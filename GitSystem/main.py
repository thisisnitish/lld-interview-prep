from vcs import VersionControlSystem
from commands.command_factory import CommandFactory

def run():
    vcs_instance = VersionControlSystem()

    commands = [
        ("add", "a.txt", "Hello"),
        ("commit", "Initial commit"),
        ("add", "b.txt", "World"),
        ("commit", "Added b.txt"),
        ("create_branch", "feature"),
        ("checkout", "feature"),
        ("add", "c.txt", "Feature"),
        ("commit", "Feature start"),
        ("rollback", 1),
        ("log",),
        ("show",)
    ]

    for cmd in commands:
        cmd_type = cmd[0]
        args = cmd[1:]
        command = CommandFactory.get_command(vcs_instance, cmd_type, *args)
        command.execute()


if __name__ == "__main__":
    run()
