from commands.command import Command

class CheckoutCommand(Command):
    def __init__(self, vcs, branch_name):
        self.vcs = vcs
        self.branch_name = branch_name

    def execute(self):
        self.vcs.switch_branch(self.branch_name)
        