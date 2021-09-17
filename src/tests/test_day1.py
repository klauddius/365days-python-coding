import day1


def test_sum_with_positive_integers():
    assert day1.addition(2, 4) == 6


def test_sum_with_negative_integers():
    assert day1.addition(-2, -4) == -6


def test_sum_with_negative_and_positive_integers():
    assert day1.addition(-2, 4) == 2


def test_sum_with_positive_floats():
    assert day1.addition(1.25, 2.15) == 3.4


def test_sum_with_negative_floats():
    assert day1.addition(-3.43, -1.15) == -4.58
