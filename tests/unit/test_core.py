import textutils.core as c

def test_remove_punctuation():
    sample_text = "Hello, team! How's everything going?"
    clean_text = c.remove_punctuation(sample_text)
    assert clean_text == "Hello team Hows everything going"
