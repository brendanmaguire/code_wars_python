from code_wars_python.pillars import pillars

def test_pillars_basic_tests():
    assert pillars(1, 10, 10) == 0
    assert pillars(2, 20, 25) == 2000
    assert pillars(11, 15, 30) == 15270