import textutils.core as c

def test_sentence_count_single_sentence():
    text = "Hello world."
    result = c.sentence_count(text)
    assert result == 1

def test_sentence_count_multiple_sentences():
    text = "Hello world. How are you? I'm fine!"
    result = c.sentence_count(text)
    assert result == 3

def test_sentence_count_with_trailing_spaces():
    text = "This is one.  This is two.   "
    result = c.sentence_count(text)
    assert result == 2

def test_sentence_count_no_punctuation():
    text = "This is just a text with no punctuation"
    result = c.sentence_count(text)
    assert result == 1  # treated as one block

def test_sentence_count_empty_string():
    text = ""
    result = c.sentence_count(text)
    assert result == 0

def test_sentence_count_none_input():
    text = None
    result = c.sentence_count(text)
    assert result == 0

def test_sentence_count_with_exclamation_only():
    text = "Wow! Amazing! Incredible!"
    result = c.sentence_count(text)
    assert result == 3

def test_sentence_count_with_question_marks():
    text = "What? Really? Yes."
    result = c.sentence_count(text)
    assert result == 3

def test_sentence_count_with_mixed_punctuation():
    text = "Wait... what?! Seriously."
    result = c.sentence_count(text)
    assert result == 3

def test_sentence_count_with_newlines():
    text = "Hello world.\nHow are you?\nI’m fine."
    result = c.sentence_count(text)
    assert result == 3
