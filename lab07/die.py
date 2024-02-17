import random


class Die:
    def __init__(self):
        self.current_value = None

    def roll(self):
        self.current_value = random.randint(1, 6)

    def get_current_value(self):
        return self.current_value
