from collections import Counter

def word_count(text: str) -> dict:

    # Convert to lowercase to make counting case-insensitive
    text = text.lower()

    # Replace punctuation with spaces
    for ch in ",.!?;:-()[]{}\"'":
        text = text.replace(ch, " ")

    # Split the text into words
    words = text.split()

    # Count occurrences
    return dict(Counter(words))