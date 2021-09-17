import day14


def test_series_resistance_empty_list():
    assert day14.series_resistance(list()) == "0 ohm"


def test_series_resistance_one_arg_in_list():
    assert day14.series_resistance([5]) == "5 ohms"


def test_series_resistance_two_args_in_list():
    assert day14.series_resistance([1, 2]) == "3 ohms"


def test_series_resistance_three_args_in_list():
    assert day14.series_resistance([1, 2, 3]) == "6 ohms"


def test_series_resistance_resulting_in_less_than_one():
    assert day14.series_resistance([0.5, 0.5]) == "1.0 ohm"


def test_examples_from_site():
    assert day14.series_resistance([1, 5, 6, 3]) == "15 ohms"
    assert day14.series_resistance([0.2, 0.3, 0.4]) == "0.9 ohm"
    assert day14.series_resistance([10, 12, 1, 10]) == "33 ohms"
    assert day14.series_resistance([10, 13, 3.8, 20, 10]) == "56.8 ohms"
    assert day14.series_resistance([0.5, 0.5]) == "1.0 ohm"
    assert day14.series_resistance([16, 30, 22.8, 4]) == "72.8 ohms"
    assert day14.series_resistance([20, 15, 32.5, 2]) == "69.5 ohms"
    assert day14.series_resistance([52, 22, 20, 30]) == "124 ohms"
    assert day14.series_resistance([10, 12, 32, 4.9, 5, 6, 71]) == "140.9 ohms"
