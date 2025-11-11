from commands.command import Command

class LogCommand(Command):
    def __init__(self, vcs):
        self.vcs = vcs

    def execute(self):
        self.vcs.logs()