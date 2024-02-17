from turn_counter import TurnCounter

def test_turn_counter_tick():
    turn_counter = TurnCounter()
    turn_counter.tick()
    assert turn_counter.get_turn() == 1 