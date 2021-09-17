import pytest
import day7


def test_triangle_base_height_with_zero():
    assert day7.tri_area(0, 0) == 0


def test_triangle_base_height_wrong_args():
    with pytest.raises(TypeError):
        day7.tri_area("1", "2")


def test_triangle_base_height_args_success():
    assert day7.tri_area(7, 4) == 14


def test_triangle_base_height_negative_args():
    assert day7.tri_area(-2, -3) == 3
