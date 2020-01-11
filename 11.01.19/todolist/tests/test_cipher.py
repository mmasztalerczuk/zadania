import pytest

from todolist.crypt import cryptChar, cryptText


def test_cipher_simple():
    assert cryptChar("A") == "X"


def test_cipher_last():
    assert cryptChar("Z") == "W"


@pytest.mark.parametrize("input_text,expected_text", [
    ("", ""),
    ("AB CD 123!@#", "XY ZA 123!@#"),
    ("ABCD", "XYZA"),
    ("AB CD 123", "XY ZA 123"),
    ("A", "X"),
])
def test_cipher_text(input_text, expected_text):
    assert cryptText(input_text) == expected_text