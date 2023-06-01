# Floors:    G     1      2        3     4      5      6         Answers:
from typing import Any

from code_wars_python.the_lift import Dinglemouse


def test_all_going_up() -> None:
    _test_the_lift(((), (), (5, 5, 5), (), (), (), ()), [0, 2, 5, 0])


def test_all_going_down() -> None:
    _test_the_lift(((), (), (1, 1), (), (), (), ()), [0, 2, 1, 0])


def test_stop_at_every_floor_going_up() -> None:
    _test_the_lift(((), (3,), (4,), (), (5,), (), ()), [0, 1, 2, 3, 4, 5, 0])


def test_stop_at_every_floor_going_down() -> None:
    _test_the_lift(((), (0,), (), (), (2,), (3,), ()), [0, 5, 4, 3, 2, 1, 0])


def _test_the_lift(queues: tuple[Any, ...], expected_answer: list[int]) -> None:
    lift = Dinglemouse(queues, 5)
    assert lift.theLift() == expected_answer
