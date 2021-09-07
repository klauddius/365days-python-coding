import day3
import pytest


def test_wrong_arg_string():
    with pytest.raises(TypeError):
        day3.num_of_digits("abc")


def test_wrong_arg_float_number():
    with pytest.raises(TypeError):
        day3.num_of_digits(23.4)


def test_wrong_arg_complex_number():
    with pytest.raises(TypeError):
        day3.num_of_digits(4j)


def test_wrong_arg_boolean():
    with pytest.raises(TypeError):
        day3.num_of_digits(True)


def test_arg_one_digit():
    assert day3.num_of_digits(2) == 1


def test_arg_two_digits():
    assert day3.num_of_digits(19) == 2


def test_arg_three_digits():
    assert day3.num_of_digits(154) == 3


def test_arg_negative_number():
    assert day3.num_of_digits(-3254) == 4


def test_arg_too_many_digits():
    assert day3.num_of_digits(12345678901234567890) == 20