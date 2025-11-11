from commands.command import Command

class SetCommand(Command):
    def __init__(self, kv_store, key, value):
        self.kv_store = kv_store
        self.key = key
        self.value = value

    def execute(self):
        self.kv_store.set(self.key, self.value)