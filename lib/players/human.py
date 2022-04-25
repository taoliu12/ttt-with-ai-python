from player import Player

class Human(Player):
    def __init__(self, token):
      self.token = token
      self.type = "human"