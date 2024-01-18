from twttr import shorten

def test_shorten():
    assert shorten("twitter") == 'twttr'
    assert shorten("Omar") == 'mr'
    # assert shorten(",sf") == 'sf'

def test_punc():
    assert shorten(',sf') == ',sf'

def test_num():
    assert shorten('1fs') == '1fs'