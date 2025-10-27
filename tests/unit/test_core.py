# tests/unit/test_core.py
import pytest
import textutils.core as c

# --- Basisfälle --------------------------------------------------------------

@pytest.mark.parametrize(
    "text, expected",
    [
        ("", 0),
        ("Hello World", 3),   # e, o, o
        ("AEIOU", 5),         # Groß/Klein egal
        ("bcdfg", 0),         # keine Vokale
        ("123?!", 0),         # Ziffern/Satzzeichen ignoriert
        ("a-b_c", 1),         # nur 'a' ist Vokal
    ],
)
def test_count_vowels_basic(text, expected):
    assert c.count_vowels(text) == expected


# --- include_y Verhalten -----------------------------------------------------

def test_does_not_count_y_by_default():
    assert c.count_vowels("rhythm") == 0

def test_counts_y_when_enabled():
    assert c.count_vowels("rhythm", include_y=True) == 1


# --- Unicode / Akzente (einfache Version zählt sie NICHT) -------------------

@pytest.mark.parametrize(
    "text, expected",
    [
        ("Café", 1),      # 'é' wird NICHT gezählt, nur 'a'
        ("ÄÖÜ äöü", 0),   # Umlaute nicht als a/e/i/o/u
    ],
)
def test_does_not_count_accented_vowels_in_simple_version(text, expected):
    assert c.count_vowels(text) == expected


# --- Fehlerfälle -------------------------------------------------------------

def test_raises_type_error_on_non_string():
    with pytest.raises(TypeError):
        c.count_vowels(None)  # type: ignore[arg-type]

def test_keyword_only_parameter_enforced():
    # include_y ist keyword-only; positionale Übergabe -> TypeError
    with pytest.raises(TypeError):
        c.count_vowels("abc", True)  # type: ignore[arg-type]
