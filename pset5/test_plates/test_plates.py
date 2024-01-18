from plates import is_valid

def test_start_with_alpha():
    assert is_valid("1234") == False
    assert is_valid('@fsf') == False


def test_length():
    assert is_valid("aaaaaaaa") == False
    assert is_valid("aaaaa") == True
    assert is_valid('a') == False

def test_punc():
    assert is_valid('aa@') == False


def test_zero_edge():
    assert is_valid('aa02') == False
    assert is_valid('aa22') == True