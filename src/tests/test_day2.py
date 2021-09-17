import pytest
import day2


def test_empty_string():
    assert day2.add_nums("") == 0


def test_string_all_spaces():
    assert day2.add_nums("    ") == 0


def test_string_without_numbers():
    with pytest.raises(ValueError):
        day2.add_nums("not a number")


def test_string_with_wrong_separator():
    with pytest.raises(ValueError):
        day2.add_nums("1#2")


def test_string_with_one_digit():
    assert day2.add_nums("1") == 1


def test_string_with_two_digits():
    assert day2.add_nums("2, 3") == 5


def test_string_with_float_numbers():
    assert day2.add_nums("1.2, 3.1") == 4.3


def test_string_too_many_numbers():
    assert (
        day2.add_nums(
            "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, "
            "19, 20"
        )
        == 210
    )
