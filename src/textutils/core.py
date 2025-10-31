import re

def sentence_count(text):
    """
    Counts the number of sentences in the given text.
    Sentences are assumed to end with '.', '!', or '?'.
    Returns 0 if text is empty or None.
    """
    if not text:
        return 0

    # Split text by sentence-ending punctuation
    sentences = re.split(r'[.!?]+', text)

    # Remove empty strings after splitting
    sentences = [s.strip() for s in sentences if s.strip()]

    return len(sentences)
