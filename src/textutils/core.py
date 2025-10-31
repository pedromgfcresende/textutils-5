# src/textutils/core.py
import re

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




