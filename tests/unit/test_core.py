
import pytest
import textutils.core as c



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
