from bank import value

def test_value():
    assert value("hello") == 0
    assert value("Hi") == 20
    assert value("whats up") == 100
