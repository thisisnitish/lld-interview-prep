from models.snake import Snake
from models.ladder import Ladder
from models.board import Board

class BoardFactory:
    @staticmethod
    def create_default_board(size=100):
        snakes = [
            Snake(99, 10),
            Snake(90, 50),
            Snake(70, 30),
        ]
        ladders = [
            Ladder(5, 25),
            Ladder(40, 60),
            Ladder(55, 90),
        ]
        return Board(size, snakes, ladders)