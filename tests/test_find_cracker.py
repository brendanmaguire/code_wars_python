from code_wars_python.find_cracker import find_hack

def test_sample_test():
    array = [
        ["name1", 150, ["B", "A", "A", "C", "A", "A"]],
        ["name2", 120, ["B", "A", "A", "A"]],
        ["name3", 160, ["B", "A", "A", "A","A"]],
        ["name4", 140, ["B", "A", "A", "C", "A"]]
    ]

    assert find_hack(array) == ["name2", "name4"]