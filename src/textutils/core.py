

def remove_punctuation(text):
    import string
    """
    Removes punctuation from the input text.

    Parameters:
    text (str): The string from which punctuation will be removed.

    Returns:
    str: Text without punctuation.
    """
    return text.translate(str.maketrans('', '', string.punctuation))



