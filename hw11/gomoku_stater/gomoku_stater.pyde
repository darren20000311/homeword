from stone import Stone
from board import Board

SIZE = 300
STROKE_WEIGHT = 5
R_OF_STONE = 32
stones = []
colorOfStone = "Black"
cellDivider = 4
cellSize = SIZE / cellDivider
board = Board(SIZE, cellDivider, cellSize, STROKE_WEIGHT)

def setup():
    size(SIZE, SIZE)
    background(235, 170, 30)
    
def draw():
    global colorOfStone
    board.display()
    
    # Draw all stones
    for stone in stones:
        stone.display()
    
def mousePressed():
    global colorOfStone
    x, y = board.get_nearest_point(mouseX, mouseY)
    if not board.is_occupied(x, y):
        new_stone = Stone(x, y, R_OF_STONE, colorOfStone)
        stones.append(new_stone)
        new_stone.display()
        colorOfStone = "White" if colorOfStone == "Black" else "Black"
        board.record_location(x, y)
        if board.stone_count >= 9:
            print("Game over!!")
