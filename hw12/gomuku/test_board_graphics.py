from board_graphics import BoardGraphics

def test_board_graphics():
    board = BoardGraphics(30, 30, 900, 60, 14)
    assert board.line_x == 30
    assert board.line_y == 30
    assert board.window_width == 900
    assert board.line_dis == 60
    assert board.size == 14
