from commands.command import Command

class BeginCommand(Command):
    def __init__(self, kv_store):
        self.kv_store = kv_store

    def execute(self):
        self.kv_store.begin()