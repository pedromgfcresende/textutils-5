
#import src.textutils.core as c 
import textutils.core as c

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