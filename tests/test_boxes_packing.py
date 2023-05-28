from code_wars_python.boxes_packing import boxes_packing


def test_basic_tests() -> None:
    assert boxes_packing([5, 7, 4, 1, 2], [4, 10, 3, 1, 4], [6, 5, 5, 1, 2]) is True
    assert boxes_packing([1, 3, 2], [1, 3, 2], [1, 3, 2]) is True
    assert boxes_packing([1, 1], [1, 1], [1, 1]) is False
    assert boxes_packing([3, 1, 2], [3, 1, 2], [3, 2, 1]) is False
    assert boxes_packing([2], [3], [4]) is True

    assert boxes_packing([6, 4], [5, 3], [4, 5]) is True
    assert boxes_packing([6, 3], [5, 4], [4, 5]) is True
    assert boxes_packing([6, 3], [5, 5], [4, 4]) is True
    assert boxes_packing([883, 807], [772, 887], [950, 957]) is True
    assert boxes_packing([6, 5], [5, 3], [4, 4]) is True
    assert boxes_packing([4, 10, 3, 1, 4], [5, 7, 4, 1, 2], [6, 5, 5, 1, 2]) is True
    assert boxes_packing([10, 8, 6, 4, 1], [7, 7, 6, 3, 2], [9, 6, 3, 2, 1]) is True
