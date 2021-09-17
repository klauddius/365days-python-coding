import day10


def test_mean_example1():
    assert day10.mean(42) == 3


def test_mean_example2():
    assert day10.mean(12345) == 3


def test_mean_example3():
    assert day10.mean(666) == 6


def test_mean_example4():
    assert day10.mean(80) == 4


def test_mean_example5():
    assert day10.mean(789) == 8


def test_mean_example6():
    assert day10.mean(417) == 4


def test_mean_example7():
    assert day10.mean(1357) == 4


def test_mean_example_negative_number():
    assert day10.mean(-789) == -8
