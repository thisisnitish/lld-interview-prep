class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self, steps):
        self.position += steps

    def set_position(self, pos):
        self.position = pos
