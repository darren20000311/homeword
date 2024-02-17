class Intersection:
    def __init__(self, INTERSECTION_PERCISE):
        self.x = 0
        self.y = 0
        self.percise = INTERSECTION_PERCISE
        self.xleft = self.x - self.percise
        self.xright = self.x + self.percise
        self.ytop = self.y - self.percise
        self.ybottom = self.y + self.percise
        
    def range_update(self, inter_x, inter_y):
        self.x = inter_x
        self.y = inter_y
        self.xleft = self.x - self.percise
        self.xright = self.x + self.percise
        self.ytop = self.y - self.percise
        self.ybottom = self.y + self.percise
        return self.xleft, self.xright, self.ytop, self.ybottom
