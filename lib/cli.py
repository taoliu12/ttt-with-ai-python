from game import Game
from board import Board

class Cli:
  def __init__(self):
    print("Best of luck!")
    newGame = Game()

  def ask_user(self):
      message = "What is your move?  Pick empty square 1-9:   "
      pick = input(message)
      print(' ')

  # def play(self):