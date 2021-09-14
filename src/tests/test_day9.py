import pytest
import day9


def test_next_edge_success_example1():
    assert day9.next_edge(8, 10) == 17


def test_next_edge_success_example2():
    assert day9.next_edge(5, 7) == 11


def test_next_edge_success_example3():
    assert day9.next_edge(9, 2) == 10


def test_next_edge_negative_integers_wrong_args():
    with pytest.raises(ValueError):
        day9.next_edge(-1, -1)



def test_next_edge_success_example4():
    assert day9.next_edge(5, 4) == 8


def test_next_edge_success_example5():
    assert day9.next_edge(8, 3) == 10


def test_next_edge_success_example6():
    assert day9.next_edge(7, 9) == 15


def test_next_edge_success_example7():
    assert day9.next_edge(10, 4) == 13


def test_next_edge_success_example8():
    assert day9.next_edge(7, 2) == 8

