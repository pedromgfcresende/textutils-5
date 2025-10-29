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

    # 1) Apostrophe komplett entfernen (z. B. "python's" -> "pythons")
    s = s.replace("'", "")

    # 2) Dezimalpunkte zwischen Ziffern entfernen (2.0 -> 20)
    s = re.sub(r'(?<=\d)\.(?=\d)', '', s)

    # 3) Übrige Punkte zu Leerzeichen machen
    s = s.replace('.', ' ')

    # 4) Alles Nicht-Alphanumerische (inkl. Whitespaces) zu "-"
    s = re.sub(r'[^a-z0-9]+', '-', s)

    # 5) Randstriche entfernen
    s = s.strip('-')

    return s



#def slugify(text):
    """
    #This function should do the following
    #- Convert all characters to lowercase
    #- Remove final dots (periods) and replaces them with spaces
    #- Replace spaces and other non-alphanumeric characters with hyphens
    #- Remove leading, trailing, and repeated hyphens
    #- Raise a ValueError if input is not a string
    #"""

    #raise NotImplementedError
