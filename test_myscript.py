# test_myscript.py

from myscrypt import is_palindrome


def test_palindrome_true():
    assert is_palindrome("Racecar") == True


def test_palindrome_false():
    assert is_palindrome("OpenAI") == False


def test_palindrome_with_spaces_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
