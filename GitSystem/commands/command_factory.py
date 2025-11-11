from commands.add_command import AddCommand
from commands.checkout_command import CheckoutCommand
from commands.commit_command import CommitCommand
from commands.log_command import LogCommand
from commands.roll_back_command import RollbackCommand
from commands.show_file_command import ShowfileCommand
from commands.create_branch_command import CreateBranchCommand


class CommandFactory:
    @staticmethod
    def get_command(vcs, cmd_type, *args):
        if cmd_type == "add":
            return AddCommand(vcs, *args)
        elif cmd_type == "commit":
            return CommitCommand(vcs, *args)
        elif cmd_type == "create_branch":
            return CreateBranchCommand(vcs, *args)
        elif cmd_type == "checkout":
            return CheckoutCommand(vcs, *args)
        elif cmd_type == "rollback":
            return RollbackCommand(vcs, *args)
        elif cmd_type == "log":
            return LogCommand(vcs, *args)
        elif cmd_type == "show":
            return ShowfileCommand(vcs)
        else:
            return ValueError("Unknown Command")