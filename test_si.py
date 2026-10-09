from si import simple_interest


def test_simple_interest():
    assert simple_interest(1000, 5, 2) == 100


def test_simple_interest_rate():
    assert simple_interest(1000, 0, 2) == 0



