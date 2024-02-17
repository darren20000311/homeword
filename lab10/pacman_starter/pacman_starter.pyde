WIDTH = 500
HEIGHT = 500
PACMAN_HEIGHT = 100
PACMAN_WIDTH = 100
SPEED = 3
x = WIDTH/2
y = HEIGHT/2
x_add = 0
y_add = 0


def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)
    fill(1.0, 1.0, 0.0)
    noStroke()

def draw():
    global x, y  # Must be declared as global
    background(0)

    x = x + x_add
    y = y + y_add
    
    # The following cases deal with when PacMan
    # is near the edge of the screen
    
    # If PacMan moves completely behond the right edge 
    if (x > WIDTH + (PACMAN_WIDTH/2)): 
        # Reset the x value to the left side
        x = PACMAN_WIDTH/2
    # If PacMan is overlapping the right edge
    elif (x > WIDTH - (PACMAN_WIDTH/2)):
        # draw a second PacMan on the left side, also
        # overlapping
        pacman(x - WIDTH, y)
    
    # If PacMan moves past the bottom edge, 
    # redraw at the top
    if (y > HEIGHT + (PACMAN_HEIGHT/2)):
        y = PACMAN_HEIGHT/2
    elif (y > HEIGHT - (PACMAN_HEIGHT/2)):
        pacman(x, y - HEIGHT)
        
    # If PacMan moves past the left edge, 
    # redraw at the right   
    if (x < -(PACMAN_WIDTH/2)): 
        x = WIDTH - (PACMAN_WIDTH/2)
    elif (x < PACMAN_WIDTH/2):
        pacman(x + WIDTH, y)
    
    # If PacMan moves past the top, redraw at bottom
    if (y < -(PACMAN_HEIGHT/2)):
        y = HEIGHT - (PACMAN_HEIGHT/2)
    elif (y < PACMAN_HEIGHT/2):
        pacman(x, y + HEIGHT)
    
    # Always draw PacMan at his real current location.
    pacman(x, y)

def pacman(x, y):
    """Draw PacMan to the screen"""
    # Use global variables as necessary
    arc(x, y, PACMAN_WIDTH, PACMAN_HEIGHT, 
        radians(45), 
        radians(315))
    
def keyPressed():
    global x_add, y_add  # Must be declared as global
    if (key == CODED):
        if (keyCode == DOWN):
            x_add = 0
            y_add = SPEED
        elif (keyCode == UP):
            x_add = 0
            y_add = -(SPEED)
        elif (keyCode == LEFT):
            x_add = -(SPEED)
            y_add = 0
        elif (keyCode == RIGHT):
            x_add = SPEED
            y_add = 0
