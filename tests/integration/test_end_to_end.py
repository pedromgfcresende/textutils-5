import textutils.core as c
import pytest

def test_complex_chain_palindrome_with_punctuation_removal_and_vowels():
    original = "Madam, in Eden, I'm Adam"
    cleaned = c.remove_punctuation(original)
    assert cleaned == "Madam in Eden Im Adam"
    palindrome_result = c.is_palindrome(cleaned)
    assert palindrome_result is True
    vowel_count = c.count_vowels(cleaned)
    assert vowel_count == 8  # m,a,a,i,e,i,a,a

def test_complex_slugify_capitalize_and_word_count():
    original = "Hello, World! Welcome to the #Python world."
    slug = c.slugify(original)
    assert slug == "hello-world-welcome-to-the-python-world"
    capitalized = c.capitalize_sentences(slug.replace('-', ' '))
    assert capitalized == "Hello world welcome to the python world"
    wc = c.word_count(capitalized)
    assert wc.get('world', 0) == 2
    assert wc.get('python', 0) == 1

def test_complex_truncate_and_average_length_on_cleaned_text():
    original = "Data science is awesome!!!"
    no_punct = c.remove_punctuation(original)
    truncated = c.truncate(no_punct, 15)
    assert truncated == "Data science..."
    avg_len = c.average_word_length(truncated)
    assert avg_len == 6 

def test_complex_count_vowels_reverse_and_palindrome():
    text = "Was it a car or a cat I saw?"
    no_punct = c.remove_punctuation(text)
    vowel_count = c.count_vowels(no_punct, include_y=True)
    assert vowel_count == 9
    reversed_text = c.reverse_string(no_punct)
    assert reversed_text == "was I tac a ro rac a ti saW"
    palindrome_check = c.is_palindrome(no_punct)
    assert palindrome_check is True

def test_complex_sentence_count_capitalize_and_word_count():
    paragraph = "hello! how are you? i hope you are well. let's test this."
    count_sentences = c.sentence_count(paragraph)
    assert count_sentences == 4
    capitalized = c.capitalize_sentences(paragraph)
    assert capitalized == "Hello! How are you? I hope you are well. Let's test this."
    wc = c.word_count(capitalized)
    assert wc.get("you", 0) == 2
    assert wc.get("hello", 0) == 1


