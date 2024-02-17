class Stone:
    def __init__(self, STONE_RADIUS, center_x, center_y, stone_color):
        self.color = stone_color
        self.r = STONE_RADIUS
        self.x = center_x
        self.y = center_y

    def display(self):
        fill(self.color)
        circle(self.x, self.y, self.r * 1.5)
