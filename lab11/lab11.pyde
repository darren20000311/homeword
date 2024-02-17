# Ping Pong Game using Processing with Python

# Constants
WIDTH = 600  # Width of the window
HEIGHT = 400  # Height of the window
PADDLE_WIDTH = 10  # Width of the paddles
PADDLE_HEIGHT = 80  # Height of the paddles
BALL_SIZE = 20  # Diameter of the ball
PADDLE_SPEED = 6  # Speed of the paddles
BALL_SPEED_X = 5  # Horizontal speed of the ball
BALL_SPEED_Y = 5  # Vertical speed of the ball

# Variables
player_y = HEIGHT / 2 - PADDLE_HEIGHT / 2  # Y position of the player's paddle
computer_y = HEIGHT / 2 - PADDLE_HEIGHT / 2  # Y position of the computer's paddle
ball_x = WIDTH / 2 - BALL_SIZE / 2  # X position of the ball
ball_y = HEIGHT / 2 - BALL_SIZE / 2  # Y position of the ball
ball_speed_x = BALL_SPEED_X  # Ball's horizontal speed
ball_speed_y = BALL_SPEED_Y  # Ball's vertical speed
player_score = 0  # Player's score
computer_score = 0  # Computer's score
game_over = False  # Flag to indicate game over

# Setup function
def setup():
    size(WIDTH, HEIGHT)
    smooth()
    noStroke()
    frameRate(60)

# Draw function
def draw():
    global player_y, computer_y, ball_x, ball_y, ball_speed_x, ball_speed_y, player_score, computer_score, game_over
    
    background(0)
    
    if not game_over:
        # Draw paddles
        fill(255)
        rect(0, player_y, PADDLE_WIDTH, PADDLE_HEIGHT)  # Player's paddle
        rect(WIDTH - PADDLE_WIDTH, computer_y, PADDLE_WIDTH, PADDLE_HEIGHT)  # Computer's paddle
        
        # Draw ball
        fill(255)
        ellipse(ball_x, ball_y, BALL_SIZE, BALL_SIZE)
        
        # Move the ball
        ball_x += ball_speed_x
        ball_y += ball_speed_y
        
        # Ball collision with top and bottom walls
        if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
            ball_speed_y *= -1
        
        # Ball collision with paddles
        if ball_x <= PADDLE_WIDTH:
            if player_y <= ball_y <= player_y + PADDLE_HEIGHT:
                ball_speed_x *= -1
            else:
                computer_score += 1
                game_over = True
        elif ball_x >= WIDTH - PADDLE_WIDTH - BALL_SIZE:
            if computer_y <= ball_y <= computer_y + PADDLE_HEIGHT:
                ball_speed_x *= -1
            else:
                player_score += 1
                game_over = True
        
        # Computer AI
        if computer_y + PADDLE_HEIGHT / 2 < ball_y:
            computer_y += PADDLE_SPEED
        elif computer_y + PADDLE_HEIGHT / 2 > ball_y:
            computer_y -= PADDLE_SPEED
        
        # Display scores
        fill(255)
        textSize(32)
        textAlign(CENTER)
        text(player_score, WIDTH / 4, 50)
        text(computer_score, WIDTH * 3 / 4, 50)
    else:
        print("Game Over!")

# Function to handle key presses
def keyPressed():
    global player_y
    
    if keyCode == UP:
        player_y -= PADDLE_SPEED
    elif keyCode == DOWN:
        player_y += PADDLE_SPEED

    # Ensure the paddle stays within the window
    player_y = constrain(player_y, 0, HEIGHT - PADDLE_HEIGHT)
