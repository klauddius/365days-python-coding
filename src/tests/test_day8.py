import day8


def test_convert_minutes_zero():
    assert day8.convert(0) == 0


def test_convert_minute_one():
    assert day8.convert(1) == 60


def test_convert_negative_minutes():
    assert day8.convert(-3) == -180
