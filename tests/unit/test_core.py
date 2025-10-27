import textutils.core as c

def test_truncate_longer_text_with_spaces():
    text = "This is a long sentence."
    result = c.truncate(text, 10)
    assert result == "This is..."

def test_truncate_n_equal_to_length_minus_one():
    text = "Python"
    result = c.truncate(text, 5)
    assert result == "Py..."

def test_truncate_n_very_large():
    text = "Short"
    result = c.truncate(text, 100)
    assert result == "Short"

def test_truncate_unicode_characters():
    text = "Café au lait"
    result = c.truncate(text, 7)
    assert result == "Café..."

def test_truncate_newline_characters():
    text = "Hello\nWorld"
    result = c.truncate(text, 5)
    assert result == "He..."

def test_truncate_exactly_three_characters():
    text = "Hello"
    result = c.truncate(text, 3)
    assert result == "Hel"

def test_truncate_zero_characters():
    text = "Hello"
    result = c.truncate(text, 0)
    assert result == ""

def test_truncate_negative_n():
    text = "Hello World"
    result = c.truncate(text, -1)
    assert result == ""
