from day20 import two_digit_sum


def test_examples_from_site():
    assert two_digit_sum(45) == 9
    assert two_digit_sum(38) == 11
    assert two_digit_sum(67) == 13


def test_two_digit_sum_one_digit_result():
    assert two_digit_sum(12) == 3


def test_two_digit_sum_two_digit_result():
    assert two_digit_sum(78) == 15


def test_two_digit_sum_argument_number_with_one_digit():
    assert two_digit_sum(0) == 0
