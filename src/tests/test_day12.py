import day12


def test_profit_margin_example1():
    assert day12.profit_margin(50, 50) == "0.0%"


def test_profit_margin_example2():
    assert day12.profit_margin(28, 39) == "28.2%"


def test_profit_margin_example3():
    assert day12.profit_margin(33, 84) == "60.7%"


def test_profit_margin_example3():
    assert day12.profit_margin(10, 15) == "33.3%"


def test_profit_margin_example4():
    assert day12.profit_margin(75, 40) == "-87.5%"


def test_profit_margin_example5():
    assert day12.profit_margin(55, 55) == "0.0%"


def test_profit_margin_example6():
    assert day12.profit_margin(9999, 10001) == "0.0%"