from models.dice import Dice

class Game:
    def __init__(self, players, board):
        self.players = players
        self.board = board
        self.dice = Dice()
        self.winner = None

    def play(self):
        while not self.winner:
            for player in self.players:
                input(f"\n{player.name}'s turn! Press Enter to roll the dice...")
                roll = self.dice.roll_dice()
                print(f"{player.name} rolled a {roll}")

                next_pos = player.position + roll
                if next_pos > self.board.size:
                    print(f"{player.name} cannot move, needs exact number to finish.")
                    continue

                next_pos = self.board.get_next_position(next_pos)
                player.set_position(next_pos)
                print(f"{player.name} moved to {player.position}")

                if player.position == self.board.size:
                    self.winner = player
                    print(f"\n{player.name} wins the game!")
                    return