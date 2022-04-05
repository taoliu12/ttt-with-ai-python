from board import Board
from player import Player
class Game:
    def __init__(self):
      self.board = Board() 
      self.board.print_board()
      self.player1 = Player("X")
      self.player2 = Player("O")
      # play()