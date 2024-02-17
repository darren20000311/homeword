import random
import time

class BotPlayer:
    def __init__(self, board_size, board):
        self.BOARD_SIZE = board_size
        self.board = board

    def make_move(self, difficulty):
        sleep_duration = random.uniform(0.3, 0.9)
        time.sleep(sleep_duration)
        
        if difficulty == "easy":
            return self._random_move()
        elif difficulty == "medium":
            return self._medium_move()
        elif difficulty == "hard":
            return self._hard_move()
        else:
            raise ValueError("Invalid difficulty level")

    def _random_move(self):
        empty_positions = [(i, j) for i in range(self.BOARD_SIZE) for j in range(self.BOARD_SIZE) if self.board[i][j] == -1]
        if empty_positions:
            return random.choice(empty_positions)
        else:
            return None


    def _medium_move(self):
        # This is a medium difficulty move that randomly selects a position adjacent to the player's last move.
        player_last_move = self._get_last_player_move()

        # Get a list of empty positions adjacent to the player's last move
        adjacent_positions = [(x, y) for x in range(player_last_move[0] - 1, player_last_move[0] + 2)
                              for y in range(player_last_move[1] - 1, player_last_move[1] + 2)
                              if 0 <= x < self.BOARD_SIZE and 0 <= y < self.BOARD_SIZE and self.board[x][y] == -1]

        if adjacent_positions:
            result = random.choice(adjacent_positions)
            return result
        else:
            return self._random_move()

    def _get_last_player_move(self):
        player_positions = []
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                if self.board[i][j] == 0:
                    player_positions.append((i, j))
                    
        if len(player_positions) == 0:
            return 0, 0
                    
        return random.choice(player_positions)
    
        
    def _hard_move(self):
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                if self.board[i][j] == -1:
                    self.board[i][j] = 1
                    if self._check_winner(1):
                        self.board[i][j] = -1
                        return i, j
                    self.board[i][j] = -1

                    self.board[i][j] = 0
                    if self._check_winner(0):
                        self.board[i][j] = -1
                        return i, j
                    self.board[i][j] = -1

        return self._random_move()
    
    def _check_winner(self, turn):
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
