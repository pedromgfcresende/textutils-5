import textutils.core as c

def test_is_palindrome_lowercase_uniword_true():
    text = 'madam'
    assert c.is_palindrome(text) == True

def test_is_palindrome_lowercase_uniword_false():
    text = 'hello'
    assert c.is_palindrome(text) == False

def test_is_palindrome_case_sensitivity_uniword_true():
    text = 'Madam'
    assert c.is_palindrome(text) == True

def test_is_palindrome_case_sensitivity_uniword_false():
    text = 'Hello'
    assert c.is_palindrome(text) == False

def test_is_palindrome_lowercase_multiword_no_punctuation_true():
    text = 'sit on a potato pan otis'
    assert c.is_palindrome(text) == True

def test_is_palindrome_lowercase_multiword_no_punctuation_false():
    text = "hello i am a student"
    assert c.is_palindrome(text) == False

def test_is_palindrome_case_sensitivity_multiword_with_punctuation_true():
    text = 'Sit on a potato pan, Otis'
    assert c.is_palindrome(text) == True

def test_is_palindrome_case_sensitivity_multiword_with_punctuation_false():
    text = "Hello, I am a student!"
    assert c.is_palindrome(text) == False

def test_is_palindrome_invalid_input():
    try:
        c.is_palindrome(None)
    except ValueError:
        assert True
    else:
        assert False, "ValueError was not raised"

def test_is_palindrome_empty_string():
    text = ''
    assert c.is_palindrome(text) == True

def test_is_palindrome_single_character():
    text = 'a'
    assert c.is_palindrome(text) == True

def test_is_palindrome_numbers_and_special_chars():
    text = '12321'
    assert c.is_palindrome(text) == True
    text2 = '12@#21'
    assert c.is_palindrome(text2) == True 

# --------------------------------------------------------

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

# --------------------------------------------------------

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
