import textutils.core as c

def test_average_simple_sentence():
    text = "Hello world"
    assert c.average_word_length(text) == 5.0 

def test_average_multiple_length_words():
    text = "Python programming is fun"
    assert c.average_word_length(text) == 6.0 

def test_average_single_word():
    text = "pytest"
    assert c.average_word_length(text) == 6.0  

def test_average_empty_string():
    text = ""
    assert c.average_word_length(text) == 0 

def test_average_with_punctuation():
    text = "Hello, world!"
    assert c.average_word_length(text) == 5.0  

def test_average_with_mixed_spacing():
    text = "a  b   c"
    assert c.average_word_length(text) == 1.0 

def test_average_numbers_in_text():
    text = "A1 B22 C333"
    assert c.average_word_length(text) == 3.0  



