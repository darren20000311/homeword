WIDTH = 500
HEIGHT = 500
PACMAN_HEIGHT = 100
PACMAN_WIDTH = 100
SPEED = 3
x = WIDTH/2
y = HEIGHT/2
x_add = 0
y_add = 0
mouth_angle = 0

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
        pacman(x - WIDTH, y, mouth_angle)
    
    # If PacMan moves past the bottom edge, 
    # redraw at the top
    if (y > HEIGHT + (PACMAN_HEIGHT/2)):
        y = PACMAN_HEIGHT/2
    elif (y > HEIGHT - (PACMAN_HEIGHT/2)):
        pacman(x, y - HEIGHT,mouth_angle)
        
    # If PacMan moves past the left edge, 
    # redraw at the right   
    if (x < -(PACMAN_WIDTH/2)): 
        x = WIDTH - (PACMAN_WIDTH/2)
    elif (x < PACMAN_WIDTH/2):
        pacman(x + WIDTH, y, mouth_angle)
    
    # If PacMan moves past the top, redraw at bottom
    if (y < -(PACMAN_HEIGHT/2)):
        y = HEIGHT - (PACMAN_HEIGHT/2)
    elif (y < PACMAN_HEIGHT/2):
        pacman(x, y + HEIGHT, mouth_angle)
    pacman(x, y, mouth_angle)

def pacman(x, y, mouth_angle):
    """Draw PacMan to the screen"""
    global x_add, y_add  # Use global variables as necessary
    mouth_angle = radians(45 * sin(millis() * 0.005))
    angle = 0  # Default angle
    
    if x_add > 0:  # Moving right
        angle = 0
    elif x_add < 0:  # Moving left
        angle = radians(180)
    elif y_add > 0:  # Moving down
        angle = radians(90)
    elif y_add < 0:  # Moving up
        angle = radians(270)

    arc(x, y, PACMAN_WIDTH, PACMAN_HEIGHT,
        angle + mouth_angle, 
        angle + radians(360 - 1 * degrees(mouth_angle)))

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
