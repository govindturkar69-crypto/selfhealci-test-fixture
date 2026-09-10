from calculator import divide, calculate_average


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    # This will crash with ZeroDivisionError - our real bug
    result = divide(10, 0)
    assert result is not None


def test_average():
    assert calculate_average([1, 2, 3]) == 2
