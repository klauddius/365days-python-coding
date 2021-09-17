import pytest
import day5


def test_empty_list():
    with pytest.raises(ValueError):
        day5.probability([], None)


def test_wrong_n_arg():
    with pytest.raises(TypeError):
        day5.probability([1, 2, 3, 4], "wrong")


def test_hundred_percent_probability():
    assert (
        day5.probability(
            [
                1,
            ],
            1,
        )
        == 100.0
    )


def test_fifty_percent_probability():
    assert day5.probability([1, 2], 2) == 50.0


def test_zero_percent_probability():
    assert day5.probability([5, 6, 7], 9) == 0.0


def test_too_many_items_in_list_for_probability():
    assert (
        day5.probability(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 10
        )
        == 55.0
    )
