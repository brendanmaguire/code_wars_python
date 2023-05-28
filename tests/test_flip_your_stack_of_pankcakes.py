from code_wars_python.flip_your_stack_of_pankcakes import flip_pancakes


def test_regular_cases() -> None:
    # Possible answers given in comments. Other answers are possible.

    assert flip_pancakes([1, 5, 8, 3]) == [2, 3, 1]
    assert flip_pancakes([5, 1, 2, 3, 4]) == [4, 3]
    assert flip_pancakes([1, 2, 3, 5, 4]) == [3, 4, 3, 2]

    assert flip_pancakes(list(range(1000, 0, -1))) == [999]

    # Duplicates
    assert flip_pancakes([2, 3, 1, 2, 4, 2]) == [4, 5, 2, 4, 1]
    assert flip_pancakes([4, 1, 3, 2, 4, 6, 3, 9, 1]) == [7, 8, 6, 7, 2, 5, 1, 4, 1, 3, 2]


def test_edge_cases() -> None:
    case1 = [1, 3, 5, 8]  # Already sorted; answer = []
    case2 = [1, 1, 1, 2, 2, 2]  # Already sorted; answer = []
    case3: list[int] = []  # No pancakes - hungry! answer = []
    case4 = [6]  # 1 pancake; answer = []

    test_cases = [case1, case2, case3, case4]

    for test_case in test_cases:
        assert flip_pancakes(test_case) == []
