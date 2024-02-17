class TurnCounter():
    def __init__(self):
        self.turn = 0
        
    def tick(self):
        self.turn = 1 - self.turn
        
    def get_turn(self):
        return self.turn
