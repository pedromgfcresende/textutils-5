from textutils.core import reverse_string

def test_reverse_basic():
    text = "hello"
    assert reverse_string(text) == "olleh"

def test_reverse_with_numbers():
    text = "abc123"
    assert reverse_string(text) == "321cba"

def test_reverse_with_spaces():
    text = "Python Test"
    assert reverse_string(text) == "tseT nohtyP"

def test_reverse_palindrome():
    text = "madam"
    assert reverse_string(text) == "madam"

def test_reverse_empty_string():
    text = ""
    assert reverse_string(text) == ""

def test_reverse_mixed_case():
    text = "AbCdEf"
    assert reverse_string(text) == "fEdCbA"

def test_reverse_with_accented():
    text = "éclair"
    assert reverse_string(text) == "rialcé"