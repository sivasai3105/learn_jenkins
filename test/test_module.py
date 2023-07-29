from src.main import Learn


def test_Learn():
    assert Learn(2, 2).fun() == 4
