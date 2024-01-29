import pytest

from vowels_counter import count_vowels

def test_count_vowels():
    assert count_vowels("Hello") == 2
    assert count_vowels("PYTHON") == 1
    assert count_vowels("bcd") == 0
    assert count_vowels("aeiou") == 5
    assert count_vowels("") == "Error: No input provided."

