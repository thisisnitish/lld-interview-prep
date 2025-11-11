from commands.command import Command

class GetCommand(Command):
    def __init__(self, kv_store, key):
        self.kv_store = kv_store
        self.key = key

    def execute(self):
        print(self.kv_store.get(self.key))