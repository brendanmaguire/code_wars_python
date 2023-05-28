# https://www.codewars.com/kata/5bb0c58f484fcd170700063d/train/python
#
# There are pillars near the road. The distance between the pillars is the same and the width of the pillars is the same. Your function accepts three arguments: # noqa: E501
#
#     number of pillars (≥ 1);
#     distance between pillars (10 - 30 meters);
#     width of the pillar (10 - 50 centimeters).
#
# Calculate the distance between the first and the last pillar in centimeters (without the width of the first and last pillar). # noqa: E501

def pillars(num_pill: int, dist: int, width: int) -> int:
    if num_pill == 1:
        return 0
    else:
        return (num_pill - 2) * width + (num_pill - 1) * (dist * 100)
