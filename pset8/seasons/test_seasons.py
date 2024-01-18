from datetime import date
from seasons import get_date, get_minutes_str
import pytest

today = date(2023,7,16)
one_year_ago = date(2022,7,16)
two_years_ago = date(2021,7,16)

def test_get_minutes_str_default():
    assert get_minutes_str(today, one_year_ago) == "Five hundred twenty-five thousand, six hundred minutes"
    assert get_minutes_str(today, two_years_ago) == "One million, fifty-one thousand, two hundred minutes"

def test_ValueError():
    with pytest.raises(ValueError):
        get_date("January 1, 1999")
    with pytest.raises(ValueError):
        get_date("first of jan, 2000")
    with pytest.raises(ValueError):
        get_date("0,0,0")