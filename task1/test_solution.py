import pytest
from solution import sum_two

def test_valid_input():
    assert sum_two(2, 3) == 5

def test_invalid_type():
    with pytest.raises(TypeError):
        sum_two(2, "3")

def test_float_type():
    with pytest.raises(TypeError):
        sum_two(2, 3.0)
