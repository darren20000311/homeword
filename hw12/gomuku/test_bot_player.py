from bot_player import BotPlayer

def test_bot_player():
    board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
    bot = BotPlayer(3, board)
    move = bot._random_move()
    assert isinstance(move, tuple)