from commands.command import Command

class ShowfileCommand(Command):
    def __init__(self, vcs):
        self.vcs = vcs

    def execute(self):
        self.vcs.show_files()
        