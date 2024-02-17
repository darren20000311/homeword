class BoardGraphics():
    def __init__(self, LINE_X, LINE_Y, WINDOW_WIDTH, LINE_DIS, BOARD_SIZE):
        self.line_x = LINE_X
        self.line_y = LINE_Y
        self.window_width = WINDOW_WIDTH
        self.line_dis = LINE_DIS
        self.size = BOARD_SIZE
        
    def display(self):
        for i in range(self.size + 1):
            y = self.line_y + i * self.line_dis
            line(self.line_x, y, self.window_width - self.line_x, y)

        for i in range(self.size + 1):
            x = self.line_x + i * self.line_dis
            line(x, self.line_y, x, self.line_y + self.size * self.line_dis)

        strokeWeight(5)
        
