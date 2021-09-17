import pytest
import day6


def test_to_list_number_zero():
    assert day6.to_list(0) == [0]


def test_to_list_negative_number():
    assert day6.to_list(-123) == ["-", 1, 2, 3]


def test_to_list_positive_number():
    assert day6.to_list(456) == [4, 5, 6]


def test_to_list_wrong_arg():
    with pytest.raises(TypeError):
        day6.to_list("test")


def test_to_number_empty_list():
    with pytest.raises(ValueError):
        day6.to_number(list())


def test_to_number_list_with_invalid_items():
    with pytest.raises(TypeError):
        day6.to_number(["t", "e", "s", "t"])


def test_to_number_list_number_zero():
    assert (
        day6.to_number(
            [
                0,
            ]
        )
        == 0
    )


def test_to_number_list_negative_number():
    assert day6.to_number(["-", 1, 2, 3]) == -123


def test_to_number_list_positive_number():
    assert day6.to_number([4, 5, 6]) == 456
