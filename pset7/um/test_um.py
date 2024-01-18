from um import count


def test_default():
    assert count("um") == 1
    assert count("um um") == 2
    assert count(" um um um ") == 3


def test_word_only():
    assert count("Um, this yummy thing is, um delicous") == 2
    assert count("umy um fsafum") == 1


def test_upper():
    assert count("um") == 1
    assert count("uM") == 1
    assert count("Um") == 1
    assert count("UM") == 1


def test_spaces():
    assert count(" um ") == 1
    assert count("um ") == 1
    assert count(" um") == 1
