from simpleinterest import simInt

def text_simpleInt_pos():
    assert simInt(2000, 8, 12) == 19200

def text_simpleInt_zer():
    assert simInt(10000, 7 ,8) == 0
