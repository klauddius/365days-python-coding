from day19 import sum_of_two


def test_examples_from_site():
    assert sum_of_two([1, 2], [4, 5, 6], 5) is True

    assert sum_of_two([1, 2], [4, 5, 6], 8) is True

    assert sum_of_two([1, 2], [4, 5, 6], 3) is False

    assert sum_of_two([1, 2], [4, 5, 6], 9) is False


def test_when_sum_of_two_exists():
    assert sum_of_two([1, 2], [1, 2, 3], 2) is True


def test_when_sum_of_two_does_not_exists():
    assert sum_of_two([1, 2], [1, 2, 3], 6) is False
