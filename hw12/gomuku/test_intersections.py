from intersections import Intersections

def test_intersections_is_around_intersections():
    intersections = Intersections(30, 30, 900, 60, 14)
    result = intersections.is_around_intersections(50, 50, 20)
    assert result == False