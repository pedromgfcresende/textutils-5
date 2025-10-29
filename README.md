# textutils-5

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
