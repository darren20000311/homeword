from stone import Stone
from intersections import Intersections

class Stones:
    def __init__(self, LINE_X, LINE_Y, WINDOW_WIDTH, LINE_DIS, BOARD_SIZE):
        self.stones = []
        self.last_stone_color = color(0, 0, 0)  
        self.inter = Intersections(LINE_X, LINE_Y, WINDOW_WIDTH, LINE_DIS, BOARD_SIZE)

    def add_stone(self, x, y, STONE_RADIUS, INTERSECTION_PERCISE):
        stone = Stone(STONE_RADIUS, x, y, self.last_stone_color)
        self.stones.append(stone)
        self.last_stone_color = stone.color  

    def display_latest(self):
        if self.stones:
            self.stones[-1].display()

    def change_color(self, new_color):
        self.last_stone_color = new_color 
        
    def is_position_occupied(self, x, y):
        for stone in self.stones:
            if stone.x == x and stone.y == y:
                return True
        return False
    
    def display_all(self):
        for stone in self.stones:
            stone.display()
            
