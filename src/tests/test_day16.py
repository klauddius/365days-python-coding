from day16 import trace


def test_square_matrix_empty():
    assert trace([[]]) == 0


def test_square_matrix_with_one_row_and_column():
    assert trace([[1]]) == 1


def test_square_matrix_with_two_rows_and_columns():
    assert trace([[1, 2], [3, 4]]) == 5


def test_square_matrix_with_three_rows_and_columns():
    assert trace([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 15


def test_examples_from_site():
    assert trace([[1, 4], [4, 1]]) == 2

    assert trace([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 15

    assert (
        trace(
            [[12345]],
        )
        == 12345
    )

    assert (
        trace([[1, 0, 1, 0], [0, 2, 0, 2], [3, 0, 3, 0], [0, 4, 0, 4]]) == 10
    )

    assert trace([[0, 1, 0, 1], [2, 0, 2, 0], [0, 3, 0, 3], [4, 0, 4, 0]]) == 0

    assert (
        trace([[1, 8, 9, 16], [2, 7, 10, 15], [3, 6, 11, 14], [4, 5, 12, 13]])
        == 32
    )
