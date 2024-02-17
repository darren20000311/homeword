from stones import Stones
from intersections import Intersections
from score_board import Scoreboard

class GameController:
    
    def __init__(self, WINDOW_HEIGHT, WINDOW_WIDTH, BOARD_SIZE):
        self.WIDTH = WINDOW_WIDTH
        self.HEIGHT = WINDOW_HEIGHT
        self.BOARD_SIZE = BOARD_SIZE + 1
        
        self.board = [[-1 for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        self.is_game_over = False
    
    def update(self):
        if self.is_game_over == False and self.check_winner(0):
            scoreboard = Scoreboard()
            scoreboard.update_score('HUMAN')
            self.game_result = 'BLACK WINS'
            self.is_game_over = True
        elif self.is_game_over == False and self.check_winner(1):
            scoreboard = Scoreboard()
            scoreboard.update_score('BOT')
            self.game_result = 'WHITE WINS'
            self.is_game_over = True
        elif self.is_game_over == False and self._get_stones_size() == self.BOARD_SIZE * self.BOARD_SIZE:
            self.game_result = 'GAME OVER'
            self.is_game_over = True
            
        if self.is_game_over:
            fill(0, 255, 0)
            textSize(80)
            text(self.game_result, (self.WIDTH - textWidth(self.game_result)) / 2, self.HEIGHT / 2)
        
    def add_stone(self, x, y, turn):
        self.board[x][y] = turn
    
    def check_winner(self, turn):
        for row in self.board:
            if self._check_sequence(row, turn):
                return True

        for col in range(self.BOARD_SIZE):
            column = [self.board[row][col] for row in range(self.BOARD_SIZE)]
            if self._check_sequence(column, turn):
                return True

        for i in range(self.BOARD_SIZE - 4):
            for j in range(self.BOARD_SIZE - 4):
                diagonal = [self.board[i + k][j + k] for k in range(5)]
                if self._check_sequence(diagonal, turn):
                    return True

                diagonal = [self.board[i + k][j + 4 - k] for k in range(5)]
                if self._check_sequence(diagonal, turn):
                    return True

        return False

    def _check_sequence(self, sequence, turn):
        consecutive_count = 0
        for stone in sequence:
            if stone == turn:
                consecutive_count += 1
                if consecutive_count == 5:
                    return True
            else:
                consecutive_count = 0

        return False
    
    def _get_stones_size(self):
        num_of_stones = 0
        for row in self.board:
            for val in row:
                if val != -1:
                    num_of_stones += 1
            
        return num_of_stones
