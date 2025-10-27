import textutils.core as c

def test_word_count_basic():
    text = "Hello hello world"
    result = c.word_count(text)
    assert result == {"hello": 2, "world": 1}

def test_word_count_with_punctuation():
    text = "Hello, world! Hello..."
    result = c.word_count(text)
    assert result == {"hello": 2, "world": 1}

def test_word_count_empty_string():
    text = ""
    result = c.word_count(text)
    assert result == {}

def test_word_count_only_punctuation():
    text = "!!! ... ???"
    result = c.word_count(text)
    assert result == {}

def test_word_count_mixed_case():
    text = "Python PYTHON python"
    result = c.word_count(text)
    assert result == {"python": 3}

def test_word_count_multiple_spaces():
    text = "  hello   world  hello   "
    result = c.word_count(text)
    assert result == {"hello": 2, "world": 1}

def test_word_count_numbers_and_words():
    text = "AI 2025 ai 2025 AI"
    result = c.word_count(text)
    assert result == {"ai": 3, "2025": 2}

def test_word_count_special_characters_inside():
    text = "high-tech high tech"
    result = c.word_count(text)
    assert result == {"high": 2, "tech": 2}

