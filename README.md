# textutils-5

--------------------------------------------------------------------------------

## Group Member: Mats Hoffmann

---

### Feature 1: `count_vowels(text, *, include_y=False)`

Counts the number of vowels (`a, e, i, o, u`) in a given text.

- Optional parameter `include_y=True` counts `'y'` as a vowel  
- Ignores case (works for uppercase and lowercase letters)  
- Raises `TypeError` if input is not a string  

**Test details:**
- Tested in: `tests/unit/test_core2.py`  
- Branch: `feat/count_vowels`  
- Status: 100 % test coverage (tested with `pytest` and parameterized tests)

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
- Status: All 8 tests passed successfully

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
- Branch: `feat/word_count`  
- Status: 100 % test coverage (all tests passed with `pytest`)  
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
- Status: 100 % test coverage (all tests passed with `pytest`)  
- Covered edge cases:
  - No punctuation → treated as one sentence  
  - Empty or `None` input → returns 0  
  - Mixed punctuation (`.`, `!`, `?`)  
  - Newlines between sentences  

---

### Shared Feature: `truncate(text: str, number_of_letters: int) -> str`

Collaborative branch developed with **pedromgfcresende**.  
Initial tests were written by **GianlucaBave**, the implementation was completed by **pedromgfcresende**, and additional tests and validations were later added by **GianlucaBave**.

- Returns a truncated version of the input string, limited to `n` characters  
- Adds `"..."` at the end if the text exceeds `n` characters, unless `n ≤ 3`  
- Handles edge cases such as:
  - `n <= 0` → returns empty string  
  - Unicode and newline characters  
  - Text shorter than `n` (returns unchanged)  
- Ensures output type consistency (`str`)  

**Test details:**
- Branch: `feat/truncate`  
- Status: 100 % test coverage (verified with `pytest`)  
- Covered edge cases:
  - Zero, negative, or very small `n` values  
  - Unicode and newline handling  
  - Text shorter or equal to the limit  
  - Trailing spaces and type checks

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
- Status: 100 % test coverage (all tests passed with `pytest`)  
- Covered edge cases:
  - Reverse basic word  
  - Numbers and text combined 
  - Mixed casing and spaces  
  - Palindromes
  - Reverse accented

---