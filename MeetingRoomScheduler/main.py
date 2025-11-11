from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor

from services.scheduler import Scheduler
from strategies.conflict_strategy import SimpleConflictCheckerStrategy


def run():
    scheduler = Scheduler(conflict_checker=SimpleConflictCheckerStrategy())
    scheduler.subscribe(lambda msg: print("[NOTIFY]", msg))

    scheduler.add_room(1, "Ocean", 4)
    scheduler.add_room(2, "Sea", 6)

    now = datetime.now().replace(minute=0, second=0, microsecond=0)
    start = now + timedelta(hours=1)
    end = start + timedelta(hours=2)

    # Simulate multiple users booking same room concurrently
    users = ["alice", "bob", "charlie", "david"]

    def try_booking(user):
        scheduler.book_room(1, user, start, end)

    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(try_booking, users)
    
    scheduler.show_schedule(1)
    scheduler.show_schedule(2)

if __name__ == "__main__":
    run()