from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    with pytest.raises(ValueError):
        convert("23.4/234")
        convert("4/3")
        convert("3,4")
    with pytest.raises(ZeroDivisionError):
        convert("3/0"           )

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(35) == "35%"
