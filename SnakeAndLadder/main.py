from services.game_service import Game
from services.board_factory import BoardFactory
from models.player import Player

def run():
    players = [Player("Alice"), Player("Bob")]
    board = BoardFactory.create_default_board()
    game = Game(players, board)
    game.play()

if __name__ == "__main__":
    run()