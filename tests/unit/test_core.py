import textutils.core as c
import pytest

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

# --------------------------------------------------------

@pytest.mark.parametrize(
    "text, expected",
    [
        ("", 0),
        ("Hello World", 3),   
        ("AEIOU", 5),         
        ("bcdfg", 0),         
        ("123?!", 0),         
        ("a-b_c", 1),         
    ],
)

def test_count_vowels_basic(text, expected):
    assert c.count_vowels(text) == expected

def test_does_not_count_y_by_default():
    assert c.count_vowels("rhythm") == 0

def test_counts_y_when_enabled():
    assert c.count_vowels("rhythm", include_y=True) == 1

@pytest.mark.parametrize(
    "text, expected",
    [
        ("Café", 1),      
        ("ÄÖÜ äöü", 0),   
    ],
)

def test_does_not_count_accented_vowels_in_simple_version(text, expected):
    assert c.count_vowels(text) == expected

def test_raises_type_error_on_non_string():
    with pytest.raises(TypeError):
        c.count_vowels(None)  

def test_keyword_only_parameter_enforced():
    
    with pytest.raises(TypeError):
        c.count_vowels("abc", True)  

# --------------------------------------------------------

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

def test_truncate_empty_string():
    text = ""
    result = c.truncate(text, 5)
    assert result == ""

def test_truncate_single_character():
    text = "A"
    result = c.truncate(text, 1)
    assert result == "A"

def test_truncate_n_less_than_three():
    text = "Testing"
    result = c.truncate(text, 2)
    assert result == "Te"

def test_truncate_with_trailing_spaces():
    text = "Hello   "
    result = c.truncate(text, 5)
    assert result == "He..."

def test_truncate_preserves_original_type():
    text = "Data"
    result = c.truncate(text, 10)
    assert isinstance(result, str)

# --------------------------------------------------------

def test_slugify_basic():
    assert c.slugify("Hello World") == "hello-world"
    assert c.slugify("Python Programming") == "python-programming"

def test_slugify_punctuation():
    assert c.slugify("Hello, World!") == "hello-world"
    assert c.slugify("Python's best!") == "pythons-best"

def test_slugify_multiple_spaces():
    assert c.slugify("Hello   World") == "hello-world"
    assert c.slugify("  Leading and trailing spaces  ") == "leading-and-trailing-spaces"

def test_slugify_numbers():
    assert c.slugify("Version 2.0") == "version-20"
    assert c.slugify("123 456 789") == "123-456-789"

def test_slugify_mixed_case():
    assert c.slugify("This is A TEST") == "this-is-a-test"

def test_slugify_symbols():
    assert c.slugify("Clean#This@Up!") == "clean-this-up"

def test_slugify_empty_string():
    assert c.slugify("") == ""

def test_slugify_non_string_input():
    
    try:
        c.slugify(123)
        assert False, 'ValueError not raised'

    except ValueError:
        assert True

# --------------------------------------------------------

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

