from services.kv_store import KVStore
from commands.command_factory import CommandFactory

def run():
    store = KVStore()

    commands = [
        ("SET", "num", 1),
        ("GET", "num"),
        ("SET", "name", "nitish"),
        ("SET", "fname", "prashant"),
        ("COUNT", 1),
        ("BEGIN",),
        ("SET", "num", 2),
        ("SET", "name", "kumar"),
        ("GET", "name"),
        ("ROLLBACK",),
        ("GET", "name"),
        ("GET", "num"),
        ("SET", "city", "lko"),
        ("GET", "city"),
        ("SET", "dist", "blr"),
        ("SET", "dist1", "lko1"),
        ("GET", "num"),
        ("END",)
    ]

    for cmd in commands:
        cmd_type = cmd[0]
        args = cmd[1:]
        if cmd_type == "END":
            print("Exiting...")
            return False
        command = CommandFactory.get_command(store, cmd_type, *args)
        command.execute()


if __name__ == "__main__":
    run()