from player import Player

class Computer(Player):
      def __init__(self, token):
        self.token = token
        self.type = "computer"