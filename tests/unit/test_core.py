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




