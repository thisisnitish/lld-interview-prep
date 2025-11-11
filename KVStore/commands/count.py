from commands.command import Command

class CountCommand(Command):
    def __init__(self, kv_store, value):
        self.kv_store = kv_store
        self.value = value

    def execute(self):
        print(self.kv_store.count(self.value))