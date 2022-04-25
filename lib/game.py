from bdb import Breakpoint
from board import Board
from players.human import Human
from players.computer import Computer

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
                    if self.best_move(combo): 
                        print(f'test combo')
                        breakpoint()
                        if self.board.moves[combo[0]] == " ":
                            print('returning 1st')
                            return combo[0]
                        elif self.board.moves[combo[1]] == " ":
                            print('returning 2nd')
                            return combo[1]
                        else:
                            print('returning 3rd')
                            return combo[2]
                breakpoint()
                return 4
                # pass
    
    def best_move(self, combo):
        if (self.board.moves[combo[0]] == self.board.moves[combo[1]] 
        or self.board.moves[combo[1]] == self.board.moves[combo[2]] 
        or self.board.moves[combo[0]] == self.board.moves[combo[2]]) and (
            self.board.moves[combo[0]] == self.current_player().token 
        or self.board.moves[combo[1]] == self.current_player().token):
            print(f'combo: {combo}')
            return combo
        else:
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



