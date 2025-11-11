class Board:
    def __init__(self, size, snakes, ladders):
        self.size = size
        self.snakes = {s.head: s.tail for s in snakes}
        self.ladders = {l.start: l.end for l in ladders}

    def get_next_position(self, position):
        if position in self.snakes:
            print(f"Oops! Bitten by snake at {position}, down to {self.snakes[position]}")
            return self.snakes[position]
        elif position in self.ladders:
            print(f"Yay! Climbed ladder at {position}, up to {self.ladders[position]}")
            return self.ladders[position]
        return position