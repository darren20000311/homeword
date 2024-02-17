class Stone:
    def __init__(self, x, y, r, colorOfStone):
        self.x = x
        self.y = y
        self.r = r
        self.colorOfStone = colorOfStone
        
    def get_location(self):
        return self.x, self.y
    
    def display(self):
        if self.colorOfStone == "White":
            fill(255)
        else:
            fill(0)
        ellipse(self.x, self.y, self.r*2, self.r*2)
    
