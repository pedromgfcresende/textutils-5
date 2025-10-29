import textutils.core as c

def test_remove_punctuation_basic():
    sample_text = "Hello, team! How's everything going?"
    clean_text = c.remove_punctuation(sample_text)
    assert clean_text == "Hello team Hows everything going"


def test_remove_punctuation_interrogation():
    sample_text = "How are you?"
    clean_text = c.remove_punctuation(sample_text)
    assert clean_text == "How are you"


def test_remove_punctuation_doublepoints():
    sample_text = "examples:"
    clean_text = c.remove_punctuation(sample_text)
    assert clean_text == "examples"


def test_remove_punctuation_comma():
    sample_text = "red, blue, green, pink"
    clean_text = c.remove_punctuation(sample_text)
    assert clean_text == "red blue green pink"


def test_remove_punctuation_at():
    sample_text = "g@briel@ hol@"
    clean_text = c.remove_punctuation(sample_text)
    assert clean_text == "gbriel hol"


def test_remove_punctuation_moneysign():
    sample_text = "$500"
    clean_text = c.remove_punctuation(sample_text)
    assert clean_text == "500"


def test_remove_punctuation_hashtag():
    sample_text = "#class #python #MIBA"
    clean_text = c.remove_punctuation(sample_text)
    assert clean_text == "class python MIBA"


def test_remove_punctuation_diagonals():
    sample_text = "code/test python/test"
    clean_text = c.remove_punctuation(sample_text)
    assert clean_text == "codetest pythontest"