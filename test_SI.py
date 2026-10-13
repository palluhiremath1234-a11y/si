from simpleinterest import simInt

def test_pos():
    assert simInt(5000, 8, 8) == 3200

def test_zero():
    assert simInt(2000, 0, 9) == 0