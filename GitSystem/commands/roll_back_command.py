from commands.command import Command

class RollbackCommand(Command):
    def __init__(self, vcs, version):
        self.vcs = vcs
        self.version = version

    def execute(self):
        self.vcs.roll_back(self.version)
        