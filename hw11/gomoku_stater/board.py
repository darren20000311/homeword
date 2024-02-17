class Board:
    def __init__(self, SIZE, cellDivider, cellSize, STROKE_WEIGHT):
        self.SIZE = SIZE
        self.cellDivider = cellDivider
        self.cellSize = cellSize
        self.STROKE_WEIGHT = STROKE_WEIGHT
        self.board_list = [[False] * self.cellSize for i in range(self.cellDivider)]
        self.stone_count = 0

        
    def is_occupied(self, x, y):
        """To check if the place is empty"""
        x = int(round(x / self.cellSize))
        y = int(round(y / self.cellSize))
        return self.board_list[x][y]
    
    def record_location(self, x, y):
        """To record the location of stones"""
        x = int(x / self.cellSize)
        y = int(y / self.cellSize)
        self.board_list[x][y] = True
        self.stone_count += 1


    def display(self):
        cellSize = self.cellSize
        stroke(0)
        strokeWeight(self.STROKE_WEIGHT)
        # Draw vertical lines
        for i in range(1, 4):
            line(cellSize * i, cellSize, cellSize * i, cellSize * 3)
            
        # Draw horizontal lines
        for i in range(1, 4):
            line(cellSize, cellSize * i, cellSize * 3, cellSize * i)
        
    def get_nearest_point(self, x, y):
        # Snap the x, y to the nearest intersection point
        newX = self.get_back_to_board(round(x / self.cellSize) * self.cellSize)
        newY = self.get_back_to_board(round(y / self.cellSize) * self.cellSize)
        return newX, newY

    def get_back_to_board(self, x):
        """get the outsiders back into the board"""
        if (x < self.cellSize):
            x = self.cellSize
        elif (x > 3 * self.cellSize):
            x = 3 * self.cellSize
        return x   
    
    
