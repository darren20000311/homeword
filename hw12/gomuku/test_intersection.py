from intersection import Intersection

def test_intersection_range_update():
    intersection = Intersection(20)
    xleft, xright, ytop, ybottom = intersection.range_update(50, 50)
    assert xleft == 30
    assert xright == 70
    assert ytop == 30
    assert ybottom == 70