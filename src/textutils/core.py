

def count_vowels(text: str, *, include_y: bool = False) -> int:
    """Count vowels (aeiou) in the given text. Set include_y=True to count 'y'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    vowels = "aeiouy" if include_y else "aeiou"
    return sum(ch in vowels for ch in text.lower())
