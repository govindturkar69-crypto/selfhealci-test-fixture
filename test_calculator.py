import pytest
from calculator import divide, calculate_average


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_average():
    assert calculate_average([1, 2, 3]) == 2