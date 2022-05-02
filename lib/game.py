from bdb import Breakpoint
from board import Board
from players.human import Human
from players.computer import Computer
import random

class Game:
    def __init__(self, num):
      self.board = Board() 
      self.players = []
      self.make_players(num)

    win_combos = (
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6))

    def make_players(self, num):
        tokens = ["X", "O"]
        for token in tokens:
            if num > 0:
                print("making a human")
                self.players.append(Human(token))
                num -= 1
            else:
                print("making a computer")
                self.players.append(Computer(token))
                num -= 1
             

    def current_player(self):
        return self.players[0] if (self.board.moves.count("X") + self.board.moves.count("O")) % 2 ==0 else self.players[1]

    def other_player(self):
        return self.players[1] if (self.board.moves.count("X") + self.board.moves.count("O")) % 2 ==0 else self.players[0]
    
    def ask_user(self):
        if self.current_player().type == "human": 
            message = "What is your move?  Pick empty square 1-9:   "
            pick = input(message)
            print(' ')

            while pick != "exit":

                if int(pick) > 0 and int(pick) < 10 and self.board.moves[int(pick)-1] == ' ' : 
                    return pick
                else:
                    message = "That was not an allowed move - Pick empty square 1-9:   "
                    pick = input(message)
                    print(' ')
                
            return pick
        else:
            if self.board.moves.count("X") + self.board.moves.count("O") == 0:
                return 5
            else:
                for combo in self.win_combos:
                    test_move = self.best_move(combo)
                    if test_move: 
                        return test_move + 1
                for combo in self.win_combos:
                   if self.combo_count(combo, self.other_player().token) == 2: 
                       for i in combo:
                           if self.board.moves[i] == " ":
                               print('two of other player', combo)
                               return i + 1

                
                
                index = random.randint(0, 8)
                count = 0
                while self.board.moves[index] != " ":
                    index = random.randint(0, 8)
                    count += 1
                print("random move:", index +1)
                return index + 1
                # pass

    # def get_combo_index_of_the_blank(self, combo):


    # have all moves and positions of 3 moves
    # look at values at the 3 positions
    # find the one that is blank 
    # return the index of that blank

    # combo.each
    #      if self.board.moves[combo[0]] == " ":
    #                 return combo[0]
    #             elif self.board.moves[combo[1]] == " ":
    #                 return combo[1]
    #             else:
    #                 return combo[2]
    

    def best_move(self, combo):
        if self.combo_count(combo, self.other_player().token) == 0:
            if self.combo_count(combo, self.current_player().token) == 2:
                print(f'combo: {combo}')
                for index in combo:
                    if self.board.moves[index] == " ":
                        return index
                # if self.board.moves[combo[0]] == " ":
                #     return combo[0]
                # elif self.board.moves[combo[1]] == " ":
                #     return combo[1]
                # else:
                #     return combo[2]
            elif self.combo_count(combo, self.current_player().token) == 1:
                    if self.board.moves[combo[0]] == self.current_player().token:
                        return combo[2]
                    elif self.board.moves[combo[2]] == self.current_player().token:
                        return combo[0]
                    elif self.board.moves[combo[1]] == self.current_player().token:
                        return combo[2]
        print('false')
        return False


    def play(self):
        while True:
            self.board.print_board()
            pick = self.ask_user()

            if pick == 'exit':
                break
            player = self.current_player()
            self.move(pick)
            status = self.check_winners()
            if status == 'draw':
                self.board.print_board()
                print("It's a draw!")
                break
            elif status == False:
                print("got the move!  ", pick)
            else:
                self.board.print_board()
                print(f"You win {player.token}!")
                break
        
    def move(self, pick):
        self.board.moves[int(pick) - 1] = self.current_player().token

    def check_winners(self):
        for combo in self.win_combos:
            if self.board.moves[combo[0]] == self.board.moves[combo[1]] and self.board.moves[combo[1]] == self.board.moves[combo[2]] and self.board.moves[combo[0]]!= " ":
                return f"winner is {combo}"
        if self.board.moves.count("X") + self.board.moves.count("O") == 9:
            return "draw"
        return False


    def combo_count(self, combo, token):
        count = 0
        for i in combo:
            if self.board.moves[i] == token:
                count +=1 
        return count
