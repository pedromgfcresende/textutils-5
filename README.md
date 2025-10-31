# Textutils

A small collaborative Python package that provides simple text utilities for common string operations and analysis

---

## Installation

1. Clone the repository:
  ```bash
  git clone https://github.com/<owner>/textutils-<team>.git
  cd textutils-<team>
  ```


2. Create the environment (with micromamba):

   ```bash
   micromamba create -f environment.yml -y
   micromamba activate textutils
   ```

3. Install the package in editable mode:

   ```bash
   pip install -e .
   ```

---

## Running Tests

To run all tests and check coverage:

```bash
pytest
```

To see detailed coverage information:

```bash
pytest --cov=src/textutils --cov-report=term-missing
```


--------------------------------------------------------------------------------

## Group Member: Mats Hoffmann

---

### Feature 1: `count_vowels(text, *, include_y=False)`

Counts the number of vowels (`a, e, i, o, u`) in a given text

- Optional parameter `include_y=True` counts `'y'` as a vowel  
- Ignores case (works for uppercase and lowercase letters)  
- Raises `TypeError` if input is not a string  

**Test details:**
- Tested in: `tests/unit/test_core.py` 
- Branch: `feat/count_vowels`  

--------------------------------------------------------------------------------

## Group Member: Gianluca Bavelloni

---

### Feature 1: `word_count(text: str) -> dict`

Counts the number of occurrences of each word in a given text.  
The function is **case-insensitive** and ignores punctuation.

- Converts text to lowercase for consistent counting  
- Replaces punctuation marks with spaces before splitting  
- Splits text into words using whitespace as delimiter  
- Returns a dictionary with each word as key and its frequency as value  
- Uses `collections.Counter` for efficient counting  

**Test details:**  
- Tested in: `tests/unit/test_core.py`  
- Branch: `feat/word_count`  

- Covered edge cases:
  - Empty strings and punctuation-only input  
  - Mixed casing and multiple spaces  
  - Numbers and words combined  
  - Hyphenated words  

---

### Feature 2: `sentence_count(text: str) -> int`

Counts the number of sentences in the input text.  
Sentences are assumed to end with `.`, `!`, or `?`. Returns `0` if the input is empty or `None`.

- Uses regular expressions (`re.split`) to separate sentences by punctuation  
- Strips extra whitespace and ignores empty strings after splitting  
- Returns the total number of valid sentence fragments  
- Handles edge cases such as trailing punctuation, newlines, or missing sentence delimiters  

**Test details:**
- Branch: `feat/sentence_count`   
- Covered edge cases:
  - No punctuation → treated as one sentence  
  - Empty or `None` input → returns 0  
  - Mixed punctuation (`.`, `!`, `?`)  
  - Newlines between sentences  

--------------------------------------------------------------------------------

## Group Member: Petter Prydz

---

### Feature 1: `reverse_string_Petter(text: str) -> dict`

Reverses all characters in the input string.  
The function is **case-insensitive** and reverses all characters, including punctuation and spaces excatly as thei appear.

- Works for words, sentences, and numbers.
- Handles punctuation and spaces correctly (e.g., "Hello!" → "!olleH").
- Returns an empty string unchanged.
- Raises TypeError if the input is not a string.
- Simple and efficient one-line reversal using Python slicing.

**Test details:**  
- Branch: `feat/reverse_String_Petter`  
- Covered edge cases:
  - Reverse basic word  
  - Numbers and text combined 
  - Mixed casing and spaces  
  - Palindromes
  - Reverse accented

--------------------------------------------------------------------------------

## Group Member: Gabriela Mendez
---
### Feature 1: `remove_punctuation(text)`

Remove all punctuation marks (`-, ., !, ?, @, etc`) from the input string. 

- Uses the built-in string.punctuation constant to define all characters to be removed.  
- Applies the translation table using the text.translate(...) method for fast, single-pass character removal. 
- Uses `collections.Counter` for efficient counting  
- Always returns the resulting string with no punctuation marks.

**Test details:**  
- Branch: `feat/remove_punctuation`  
- Covered edge cases:
  - Punctuation in more than one sentence 
  - Remove question mark
  - Remove double points  
  - Remove comma
  - Remove money sign
  - Remove hashtag
  - Remove diagonals  
  - Remove " @ "

--------------------------------------------------------------------------------

## Group Member: Pedro Resende

---

### Feature 1: is_palindrome(text)

Checks if a given text is a palindrome (ignoring case, punctuation, and spaces).

- Accepts strings and numbers (converts numbers to strings)
- Raises ValueError if input is not a string or number
- Returns True if the cleaned text reads the same forwards and backwards

**Test details:**  
- Branch: `feat/is_palindrome` 

---

## Feature 2: average_word_length(text)

Calculates the average length of words in a given text, considering only letters and numbers.

- Splits text into words using whitespace
- Counts only letters and numbers in each word
- Returns the average length rounded to the nearest integer

**Test details:**  
- Branch: `feat/average_word_length` 

--------------------------------------------------------------------------------

## Shared Features: 

---

### Shared Feature: `slugify(text)`

- Converts all characters to lowercase  
- Removes dots and replaces them with spaces  
- Replaces spaces and non-alphanumeric characters with hyphens (`-`)  
- Removes leading, trailing, and repeated hyphens  
- Raises `ValueError` if the input is not a string  

**Test details:**
- Tested in: `tests/unit/test_core.py`  
- Branch: `feat/slugify`  

---

### Shared Feature: `truncate(text: str, number_of_letters: int) -> str`

- Returns a truncated version of the input string, limited to `n` characters  
- Adds `"..."` at the end if the text exceeds `n` characters, unless `n ≤ 3`  
- Handles edge cases such as:
  - `n <= 0` → returns empty string  
  - Unicode and newline characters  
  - Text shorter than `n` (returns unchanged)  
- Ensures output type consistency (`str`)  

**Test details:**
- Branch: `feat/truncate`  
- Covered edge cases:
  - Zero, negative, or very small `n` values  
  - Unicode and newline handling  
  - Text shorter or equal to the limit  
  - Trailing spaces and type checks

---

### Shared Feature: `capitalize_sentences(text: str) -> str:`

- Ensures that the first letter of each sentence is capitalized.   
- Convert the entire string to lowercase for consistency
- Define sentence separators, " . , ! , ?"
- Iterate through the string, looking for sentence enders 

**Test details:**
- Branch: `feat/capitalize_sentences`  
- Covered edge cases:
  - Capitalized first world of one sentence
  - Capitalize the first word after exclamation mark 
  - Capitalize the first word after regular point 
  - Capitalize the first word after question mark 

--------------------------------------------------------------------------------

# Team

- Pedro Resende: https://github.com/pedromgfcresende
- Gabriela Mendez: https://github.com/gabrielamendez22
- Gianluca Bavelloni: https://github.com/GianlucaBave
- Petter Prydz: https://github.com/petterprydz
- Mats Hoffmann: https://github.com/Matshoffmann






