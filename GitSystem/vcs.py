from models.commit import Commit

class VersionControlSystem:
    def __init__(self):
        self.files = {}
        self.branches = {"main": []} # {branch: [...commit]}
        self.current_branch = "main"
        self.commit_index = {"main": -1} #{branch: idx}

    def add_file(self, filename, content):
        self.files[filename] = content
        print(f"Added file {filename}")

    def commit(self, messgae):
        commit = Commit(message=messgae, files=self.files)
        self.branches[self.current_branch].append(commit)
        self.commit_index[self.current_branch] += 1
        print(f"Changed Committed: {messgae}")

    def create_branch(self, branch_name):
        if branch_name in self.branches:
            print("Branch already exists!!")
            return
        
        self.branches[branch_name] = self.branches[self.current_branch][:]
        self.commit_index[branch_name] = self.commit_index[self.current_branch]
        print(f"Branch {branch_name} created!!")

    def switch_branch(self, branch_name):
        if branch_name not in self.branches:
            print("Branch doesn't exists!!")
            return
        
        if branch_name == self.current_branch:
            print("Already in this branch!!")
            return
        
        self.current_branch = branch_name
        commit_idx = self.commit_index[branch_name]
        if commit_idx >= 0:
            self.files = self.branches[branch_name][commit_idx].files.copy()
        else:
            self.files = {}
        
        print(f"Switches to branch {branch_name}")

    
    def roll_back(self, version):
        """
        Lets you revert a branch to an earlier commit
        """
        if version < 0 or version > self.commit_index[self.current_branch]:
            print("Invalid version number!!")
            return
        
        self.commit_index[self.current_branch] = version
        self.branches[self.current_branch] = self.branches[self.current_branch][:version+1]
        self.files = self.branches[self.current_branch][version].files.copy()
        print(f"Rolled back to version {version}")

    def logs(self):
        # print(enumerate(self.branches[self.current_branch]))
        for commit in self.branches[self.current_branch]:
        # for idx, commit in enumerate(self.branches[self.current_branch]):
            print(f"Commit Messages:: {commit.message}")

    def show_files(self):
        print(f"Files in branch '{self.current_branch}':")

        for fname, content in self.files.items():
            print(f" {fname}: {content}")
        
        