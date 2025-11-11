from commands.set import SetCommand
from commands.get import GetCommand
from commands.delete import DeleteCommand
from commands.count import CountCommand
from commands.begin import BeginCommand
from commands.commit import CommitCommand
from commands.rollback import RollbackCommand

class CommandFactory:
    @staticmethod
    def get_command(kv_store, cmd_type, *args):
        if cmd_type == "SET":
            return SetCommand(kv_store, *args)
        elif cmd_type == "GET":
            return GetCommand(kv_store, *args)
        elif cmd_type == "DELETE":
            return DeleteCommand(kv_store, *args)
        elif cmd_type == "COUNT":
            return CountCommand(kv_store, *args)
        elif cmd_type == "BEGIN":
            return BeginCommand(kv_store, *args)
        elif cmd_type == "COMMIT":
            return CommitCommand(kv_store, *args)
        elif cmd_type == "ROLLBACK":
            return RollbackCommand(kv_store, *args)
        # elif cmd_type == "END":
        #     print("Exiting...")
        #     return False
        else:
            print(cmd_type)
            raise ValueError("Unknown Command")