# Pat Programmer is worried about the future of jobs in programming because of the advance of AI
# tools like ChatGPT, and he decides to become a chef instead! So he wants to be an expert at
# flipping pancakes.
#
# A pancake is characterized by its diameter, a positive integer. Given a stack of pancakes, how
# can they be arranged in order by diameter, with the largest pancake at the bottom and the
# smallest at the top? You can insert a spatula under any pancake and then flip, which reverses
# the order of all the pancakes on top of the spatula.
#
# Task
#
# Write a function that takes a stack of pancakes and returns a sequence of flips that arranges
# them in order by diameter, with the largest pancake at the bottom and the smallest at the top.
# The pancakes are given as a list of positive integers, with the left end of the list being the
# top of the stack.
#
# Based on Problem 4.6.2 in Skiena & Revilla, "Programming Challenges".
#
# Example
#
# Consider the stack [1,5,8,3]. One way of achieving the desired order is as follows:
#
# The 8 is the biggest, so it should be at the bottom. Put the spatula under it (position 2 in
# the list) and flip.
#
# This transforms the stack into [8,5,1,3], with the 8 at the top. Then flip the entire stack
# (spatula position 3).
#
# This transforms the stack into [3,1,5,8], which has the 8 at the bottom. And since the 5 is in
# the correct position as well, now flip the 1 and 3 (spatula position 1).
#
# The stack is now [1,3,5,8], as desired. The function should return [2,3,1].
# Note
#
# You don't have to find the shortest sequence of flips. That is a hard problem - see
# https://en.wikipedia.org/wiki/Pancake_sorting. However, don't include unnecessary flips, in the
# following sense:
#
# (1) If 2 consecutive flips leave the stack in the same state, they should be omitted. For
# example, [2,3,2,2,1] also arranges [1,5,8,3] correctly, but 2,2 is unnecessary.
#
# (2) Flipping only the top pancake doesn't achieve anything.
#
# Performance should not be a issue. If Pat can flip 1,000 pancakes with diameters between 1 and
# 1,000, he thinks he can get a job!

def flip_pancakes(stack: list[int]) -> list[int]:
    return list(filter(lambda flip: flip != 0, _flip_remaining_pancakes([], stack)))


def _flip_remaining_pancakes(flips: list[int], remaining_pancakes: list[int]) -> list[int]:
    if remaining_pancakes == sorted(remaining_pancakes):
        return flips

    if not remaining_pancakes:
        return flips

    biggest_remaining_pancake_size = max(remaining_pancakes)
    bottom_pancake_size = remaining_pancakes[len(remaining_pancakes) - 1]

    if bottom_pancake_size == biggest_remaining_pancake_size:
        # The biggest is already at the bottom. No flipping needed
        return _flip_remaining_pancakes(flips, remaining_pancakes[:-1])
    else:
        level_of_biggest_pancake = remaining_pancakes.index(biggest_remaining_pancake_size)
        new_remaining_pancakes = \
            list(reversed(remaining_pancakes[level_of_biggest_pancake + 1:])) \
            + remaining_pancakes[:level_of_biggest_pancake]

        return _flip_remaining_pancakes(
            flips + [level_of_biggest_pancake, len(remaining_pancakes) - 1],
            new_remaining_pancakes
        )
