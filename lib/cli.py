from game import Game
from board import Board
# from player import Player

class Cli:
  def __init__(self):
    print("Best of luck!")
    self.start()

  def start(self):
      print('Welcome to Tic-Tac-Toe')

      while True:
            num = -1
            while num < 0 or num > 2:
              print("")
              print("please enter 0-2")
              print("")
              num = int(input('How many Humans are playing this game?  '))
              print("") 

            newGame = Game(num)
            newGame.play()

            response = input("Do you want to play again?  ")
            while response.lower() != "no" and response.lower() != "yes":
                print("That is not a response I understand")
                response = input("Do you want to play again?  ")
            
            if response.lower() == "no":
                print("Bye!")
                break
            





