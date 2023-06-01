# Synopsis
#
# A multi-floor building has a Lift in it.
#
# People are queued on different floors waiting for the Lift.
#
# Some people want to go up. Some people want to go down.
#
# The floor they want to go to is represented by a number (i.e. when they enter the Lift this is
# the button they will press)
#
# BEFORE (people waiting in queues)               AFTER (people at their destinations)
#                    +--+                                          +--+
#   /----------------|  |----------------\        /----------------|  |----------------\
# 10|                |  | 1,4,3,2        |      10|             10 |  |                |
#   |----------------|  |----------------|        |----------------|  |----------------|
#  9|                |  | 1,10,2         |       9|                |  |                |
#   |----------------|  |----------------|        |----------------|  |----------------|
#  8|                |  |                |       8|                |  |                |
#   |----------------|  |----------------|        |----------------|  |----------------|
#  7|                |  | 3,6,4,5,6      |       7|                |  |                |
#   |----------------|  |----------------|        |----------------|  |----------------|
#  6|                |  |                |       6|          6,6,6 |  |                |
#   |----------------|  |----------------|        |----------------|  |----------------|
#  5|                |  |                |       5|            5,5 |  |                |
#   |----------------|  |----------------|        |----------------|  |----------------|
#  4|                |  | 0,0,0          |       4|          4,4,4 |  |                |
#   |----------------|  |----------------|        |----------------|  |----------------|
#  3|                |  |                |       3|            3,3 |  |                |
#   |----------------|  |----------------|        |----------------|  |----------------|
#  2|                |  | 4              |       2|          2,2,2 |  |                |
#   |----------------|  |----------------|        |----------------|  |----------------|
#  1|                |  | 6,5,2          |       1|            1,1 |  |                |
#   |----------------|  |----------------|        |----------------|  |----------------|
#  G|                |  |                |       G|          0,0,0 |  |                |
#   |====================================|        |====================================|
#
# Rules
# Lift Rules
#
#     The Lift only goes up or down!
#     Each floor has both UP and DOWN Lift-call buttons (except top and ground floors which have
#     only DOWN and UP respectively)
#     The Lift never changes direction until there are no more people wanting to get on/off in the
#     direction it is already travelling
#     When empty the Lift tries to be smart. For example,
#     If it was going up then it may continue up to collect the highest floor person wanting to
#     go down
#     If it was going down then it may continue down to collect the lowest floor person wanting
#     to go up
#     The Lift has a maximum capacity of people
#     When called, the Lift will stop at a floor even if it is full, although unless somebody
# gets off nobody else can get on!
#     If the lift is empty, and no people are waiting, then it will return to the ground floor
#
# People Rules
#
#     People are in "queues" that represent their order of arrival to wait for the Lift
#     All people can press the UP/DOWN Lift-call buttons
#     Only people going the same direction as the Lift may enter it
#     Entry is according to the "queue" order, but those unable to enter do not block those
#     behind them that can
#     If a person is unable to enter a full Lift, they will press the UP/DOWN Lift-call button
#     again after it has departed without them
#
# Kata Task
#
#     Get all the people to the floors they want to go to while obeying the Lift rules and the
#     People rules
#     Return a list of all floors that the Lift stopped at (in the order visited!)
#
# NOTE: The Lift always starts on the ground floor (and people waiting on the ground floor may
#       enter immediately)
# I/O
# Input
#
#     queues a list of queues of people for all floors of the building.
#     The height of the building varies
#     0 = the ground floor
#     Not all floors have queues
#     Queue index [0] is the "head" of the queue
#     Numbers indicate which floor the person wants go to
#     capacity maximum number of people allowed in the lift
#
# Parameter validation - All input parameters can be assumed OK. No need to check for things like:
#
#     People wanting to go to floors that do not exist
#     People wanting to take the Lift to the floor they are already on
#     Buildings with < 2 floors
#     Basements
#
# Output
#
#     A list of all floors that the Lift stopped at (in the order visited!)
from enum import Enum


class Dinglemouse(object):
    def __init__(self, queues: tuple[tuple[int, ...], ...], capacity: int):
        self.queues = queues
        self.capacity = capacity

    def theLift(self) -> list[int]:
        return _determine_lift_stop_order(
            [list(people_waiting_on_floor) for people_waiting_on_floor in self.queues],
            self.capacity,
        )


class Direction(Enum):
    UP = 1
    DOWN = 2


def _determine_lift_stop_order(queues: list[list[int]], capacity: int) -> list[int]:
    direction = Direction.UP
    floor = 0
    top_floor = len(queues) - 1
    lift_occupants: list[int] = []
    floors_stopped_at = [0]

    while lift_occupants or any(queues):
        stopped_at_this_floor = False

        # Drop people off
        new_lift_occupants = [
            lift_occupant for lift_occupant in lift_occupants
            if lift_occupant != floor
        ]
        if len(new_lift_occupants) != len(lift_occupants):
            stopped_at_this_floor = True
        lift_occupants = new_lift_occupants

        # Change direction if at the end
        if direction == Direction.UP and floor == top_floor:
            direction = Direction.DOWN
        elif direction == Direction.DOWN and floor == 0:
            direction = Direction.UP

        # Pick up people if there is capacity
        people_waiting_on_this_floor = queues[floor]
        available_spaces = capacity - len(lift_occupants)
        for person in people_waiting_on_this_floor.copy():
            if (direction == Direction.UP and person > floor
                    or direction == Direction.DOWN and person < floor):
                stopped_at_this_floor = True

                if available_spaces:
                    people_waiting_on_this_floor.remove(person)
                    lift_occupants.append(person)
                    available_spaces -= 1

        if stopped_at_this_floor and floors_stopped_at[-1:] != [floor]:
            floors_stopped_at.append(floor)

        # Continue to next floor
        if direction == Direction.UP:
            floor += 1
        else:
            floor -= 1

    if floors_stopped_at[-1:] != [0]:
        # Only append 0 if the lift hasn't just dropped someone off on the bottom floor
        floors_stopped_at.append(0)

    return floors_stopped_at
