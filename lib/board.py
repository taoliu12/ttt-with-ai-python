class Board:
  def __init__(self):
      self.moves = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

  def print_board(self):
    print('   |   |   ')
    print(f' {self.moves[0]} | {self.moves[1]} | {self.moves[2]} ')
    print('   |   |   ')
    print('---|---|---')
    print('   |   |   ')
    print(f' {self.moves[3]} | {self.moves[4]} | {self.moves[5]} ')
    print('   |   |   ')
    print('---|---|---')
    print('   |   |   ')
    print(f' {self.moves[6]} | {self.moves[7]} | {self.moves[8]} ')
    print('   |   |   ')
    print(' ')