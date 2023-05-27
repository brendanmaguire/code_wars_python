# https://www.codewars.com/kata/59f70440bee845599c000085

# Someone was hacking the score. Each student's record is given as an array The objects in the array are given again as an array of scores for each name and total score. ex>
#
# array = [
#   ["name1", 445, ["B", "A", "A", "C", "A", "A"]],
#   ["name2", 110, ["B", "A", "A", "A"]],
#   ["name3", 200, ["B", "A", "A", "C"]],
#   ["name4", 200, ["A", "A", "A", "A", "A", "A", "A"]]
# ]
#
# The scores for each grade is:
#
#     A: 30 points
#     B: 20 points
#     C: 10 points
#     D: 5 points
#     Everything else: 0 points
#
# If there are 5 or more courses and all courses has a grade of B or above, additional 20 points are awarded. After all the calculations, the total score should be capped at 200 points.
#
# Returns the name of the hacked name as an array when scoring with this rule.
#
# array = [
#   ["name1", 445, ["B", "A", "A", "C", "A", "A"]],     # name1 total point is over 200 => hacked
#   ["name2", 110, ["B", "A", "A", "A"]],               # name2 point is right
#   ["name3", 200, ["B", "A", "A", "C"]],               # name3 point is 200 but real point is 90 => hacked
#   ["name4", 200, ["A", "A", "A", "A", "A", "A", "A"]] # name4 point is right
# ];
#
# return ["name1", "name3"]

def find_hack(arr):
    return [name for (name, score, grades) in arr if score != min(200, _calculate_score(grades))]

def _calculate_score(grades):
    return sum(map(_grade_to_score, grades)) + _bonus(grades)

def _grade_to_score(grade):
    match grade:
        case 'A':
            return 30
        case 'B':
            return 20
        case 'C':
            return 10
        case 'D':
            return 5
        case _:
            return 0

def _bonus(grades):
    if len(grades) >= 5 and all(grade == 'A' or grade == 'B' for grade in grades):
        return 20
    else:
        return 0