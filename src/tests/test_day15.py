import pytest

import day15


def test_unique_in_the_beginning():
    assert day15.unique([1, 2, 2, 2]) == 1


def test_unique_in_the_middle():
    assert day15.unique([2, 2, 2, 3, 2, 2, 2]) == 3


def test_unique_in_the_end():
    assert day15.unique([3, 3, 3, 3, 3, 4]) == 4


def test_unique_no_unique_included_error():
    with pytest.raises(ValueError):
        day15.unique([1, 1, 1, 1, 1])


def test_unique_negative_numbers():
    assert day15.unique([-1, -1, -1, -2, -1]) == -2


def test_examples_from_site():
    assert day15.unique([3, 3, 3, 7, 3, 3]) == 7

    assert day15.unique([3, 3, 3, 3, 3, 7]) == 7

    assert day15.unique([0, 0, 0.77, 0, 0]) == 0.77

    assert day15.unique([9, 1, 1, 1, 1, 1, 1, 1]) == 9

    assert day15.unique([1, 2, 1, 1, 1, 1, 1, 1]) == 2

    assert day15.unique([3, 3, 3, 7, 3, 3]) == 7

    assert day15.unique([0, 0, 0.77, 0, 0]) == 0.77

    assert day15.unique([0, 1, 1, 1, 1, 1, 1, 1]) == 0

    assert day15.unique([-4, -4, -4, 4]) == 4

    assert day15.unique([8, 8, 8, 8, 8, 8, 8, 0.5]) == 0.5

    assert day15.unique([2, 1, 2, 2, 2, 2, 2, 2]) == 1
