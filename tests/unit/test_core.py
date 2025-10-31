import textutils.core as c

def test_capitalize_sentences_at_begging():
    sample_text = "hello team!"
    clean_text = c.capitalize_sentences(sample_text)
    assert clean_text == "Hello team!"


def test_capitalize_sentences_after_exclamation_mark():
    sample_text = "Hello team! how are you?"
    clean_text = c.capitalize_sentences(sample_text)
    assert clean_text == "Hello team! How are you?"


def test_capitalize_sentences_after_point():
    sample_text = "Hello world. my name is Carlas."
    clean_text = c.capitalize_sentences(sample_text)
    assert clean_text == "Hello world. My name is carlas."
   

def test_capitalize_sentences_after_question():
    sample_text = "Hello? are you home?"
    clean_text = c.capitalize_sentences(sample_text)
    assert clean_text == "Hello? Are you home?"
