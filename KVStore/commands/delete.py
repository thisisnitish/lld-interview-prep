from commands.command import Command

class DeleteCommand(Command):
    def __init__(self, kv_store, key):
        self.kv_store = kv_store
        self.key = key

    def execute(self):
        self.kv_store.delete(self.key)