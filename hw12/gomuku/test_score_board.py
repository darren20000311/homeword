from score_board import Scoreboard

def test_score_board_update_score():
    scoreboard = Scoreboard('test_scores.txt')
    scoreboard.update_score('HUMAN')
    assert scoreboard.scores['HUMAN'] == 1