# test_my_module.py
from my_module import is_even

def test_even_number():
    assert is_even(2) is True

def test_zero_is_even():
    assert is_even(0) is True

def test_negative_even_number():
    assert is_even(-4) is True
