from day18 import find_odd


def test_examples_from_site():
    assert find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) == -1
    # 5
    assert find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) == 5
    # 10
    assert find_odd([10]) == 10


def test_find_odd_positive_number():
    assert find_odd([1, 2, 1, 2, 3]) == 3


def test_find_odd_negative_number():
    assert find_odd([-1, -1, -2, -2, -3]) == -3


def test_find_odd_no_odd_number():
    assert find_odd([-1, -1, 2, 2, 4, 4]) is None
