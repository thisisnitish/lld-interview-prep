from commands.command import Command

class CommitCommand(Command):
    def __init__(self, vcs, message):
        self.vcs = vcs
        self.message = message

    def execute(self):
        self.vcs.commit(self.message)