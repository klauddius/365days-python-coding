import day4


def test_string_with_one_letter_d():
    assert day4.count_d('Just one letter d') == 1


def test_string_without_letter_d():
    assert day4.count_d('Only other letters') == 0


def test_string_full_of_letter_d():
    assert day4.count_d('dddDD') == 5


def test_string_with_upper_letter_d():
    assert day4.count_d('Upper letter D') == 1


def test_string_with_lower_letter_d():
    assert day4.count_d('Lower letter d') == 1

