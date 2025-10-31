import re
import string
from collections import Counter

def is_palindrome(text):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    inversed = ''
    cleaned_text = ''

    if isinstance(text, int):
        text = str(text)

    if not isinstance(text, str):
        raise ValueError('It should be an word / phrase / number')
    
    for i in range(len(text)):
        if text[i].lower() in letters:
            inversed = text[i].lower() + inversed
            cleaned_text = cleaned_text + text[i].lower()
        
        elif text[i].lower() in numbers:
            inversed = text[i].lower() + inversed
            cleaned_text = cleaned_text + text[i].lower()


    return inversed == cleaned_text

# -------------------------------------------------------------------

def average_word_length(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
    lista = text.split()
    number_of_words = len(lista)
    if number_of_words == 0:
        return 0
    a = 0
    for word in lista:
        for letter in word:
            if letter.lower() in alphabet or letter in numbers:
                a +=1
            else:
                continue
    
    return round(a/number_of_words)

# -------------------------------------------------------------------

def remove_punctuation(text):

    """
    Removes punctuation from the input text.

    Parameters:
    text (str): The string from which punctuation will be removed.

    Returns:
    str: Text without punctuation.
    """
    return text.translate(str.maketrans('', '', string.punctuation))

# -------------------------------------------------------------------

def count_vowels(text: str, *, include_y: bool = False) -> int:
    """Count vowels (aeiou) in the given text. Set include_y=True to count 'y'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    vowels = "aeiouy" if include_y else "aeiou"
    return sum(ch in vowels for ch in text.lower())

# -------------------------------------------------------------------

def truncate(text, number_of_letters):
    
    """
    Returns a truncated version of the input string, cutting it off at n characters. 
    If the string exceeds n characters, the output ends with "..." 
    unless n is less than or equal to 3, in which case only the first n characters are returned without ellipsis. 
    If n is zero or negative, returns an empty string. 
    Special cases such as unicode and newline characters are handled as regular characters, and the function expects a string as input
    
    """

    if number_of_letters <= 0:
        return ''
    
    if len(text) <= number_of_letters:
        return text
    
    if number_of_letters <= 3:

        return text[:number_of_letters]

    words = text.split()
    output = ''
    for word in words:
        if output:
            if len(output) + 1 + len(word) + 3 > number_of_letters:
                return output + '...'
            output += ' ' + word
        else:
            if len(word) + 3 > number_of_letters:
                return word[:number_of_letters - 3] + '...'
            output = word

    return output

# -------------------------------------------------------------------

def slugify(text):
    
    """
    - Convert all characters to lowercase
    - Remove final dots (periods) and replaces them with spaces
    - Replace spaces and other non-alphanumeric characters with hyphens
    - Remove leading, trailing, and repeated hyphens
    - Raise a ValueError if input is not a string
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    s = text.lower()
    s = s.replace("'", "")
    s = re.sub(r'(?<=\d)\.(?=\d)', '', s)
    s = s.replace('.', ' ')
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = s.strip('-')

    return s

# -------------------------------------------------------------------

def word_count(text: str) -> dict:

    text = text.lower()

    for ch in ",.!?;:-()[]{}\"'":
        text = text.replace(ch, " ")

    words = text.split()

    return dict(Counter(words))

# -------------------------------------------------------------------

def reverse_string(text):
    return text[::-1]
