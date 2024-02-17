from board_graphics import BoardGraphics
from intersections import Intersections
from stones import Stones
from gamecontroller import GameController
from turn_counter import TurnCounter
from bot_player import BotPlayer
import time

WINDOW_HEIGHT = 900
WINDOW_WIDTH = 900
BOARD_SIZE = 15

LINE_X = 30
LINE_Y = 30
LINE_DIS = (WINDOW_HEIGHT - LINE_X - LINE_Y) / BOARD_SIZE
INTERSECTION_PERCISE = 20
mousex = 0
mousey = 0
STONE_RADIUS = int((LINE_DIS )/2)
is_mouse_pressed = False
turn_counter = TurnCounter()
current_color = color(0, 0, 0)

board = BoardGraphics(LINE_X, LINE_Y, WINDOW_WIDTH, LINE_DIS, BOARD_SIZE)
stones = Stones(LINE_X, LINE_Y, WINDOW_WIDTH, LINE_DIS, BOARD_SIZE)
intersections = Intersections(LINE_X, LINE_Y, WINDOW_WIDTH, LINE_DIS, BOARD_SIZE)
game_controller = GameController(WINDOW_HEIGHT, WINDOW_WIDTH, BOARD_SIZE)

sleep_buffer = 0

def setup():  
    size(WINDOW_HEIGHT, WINDOW_WIDTH)
    frameRate(60)

    
def draw():
    global current_color, sleep_buffer
    background(235, 170, 30)
    board.display()
    stones.display_all()
    
    if game_controller.is_game_over == False and turn_counter.get_turn() == 1 and sleep_buffer == 2:
        turn_counter.tick()
        bot = BotPlayer(BOARD_SIZE + 1, game_controller.board)
        pos_x, pos_y = bot.make_move("medium")
        inter_x, inter_y = pos_x * LINE_DIS + LINE_X, pos_y * LINE_DIS + LINE_Y
        stones.change_color(color(255, 255, 255))
        stones.add_stone(inter_x, inter_y, STONE_RADIUS, INTERSECTION_PERCISE)
        game_controller.add_stone(pos_x, pos_y, 1)
        stones.display_latest()
        
    sleep_buffer = (sleep_buffer + 1) % 10
        
    game_controller.update()
    

def mousePressed():
    global is_mouse_pressed, mousex, mousey
    is_mouse_pressed = True
    mousex = mouseX
    mousey = mouseY

def mouseReleased():
    global is_mouse_pressed, current_color, mousex, mousey, game_controller
    is_mouse_pressed = False
    mousex = mouseX
    mousey = mouseY
    inter_x, inter_y = intersections.find_nearest_intersections( mousex, mousey, INTERSECTION_PERCISE)
    pos_x, pos_y = (inter_x - LINE_X) // LINE_DIS, (inter_y - LINE_Y) // LINE_DIS
    turn = turn_counter.get_turn()
    
    if game_controller.is_game_over:
        return
    
    if turn == 1:
        return

    if intersections.is_around_intersections(mousex, mousey, INTERSECTION_PERCISE) and not stones.is_position_occupied(inter_x, inter_y):
        stones.change_color(color(0, 0, 0))
        stones.add_stone(inter_x, inter_y, STONE_RADIUS, INTERSECTION_PERCISE)
        game_controller.add_stone(pos_x, pos_y, turn)
        turn_counter.tick()
            
    else:
        pass
        
    
    
