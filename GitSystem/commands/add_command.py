from commands.command import Command

class AddCommand(Command):
    def __init__(self, vcs, filename, content):
        self.vcs = vcs
        self.filename = filename
        self.content = content

    def execute(self):
        self.vcs.add_file(self.filename, self.content)
        