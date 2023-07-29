import pytest
pytestmark = [pytest.mark.smoke, pytest.mark.strtest]

@pytest.mark.siva
def test_a1():
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1

@pytest.mark.siva
@pytest.mark.sai
def test_a2():
    assert 9 / 5 == 1.8, "Failed Test Intentionally"




@pytest.mark.hello
def test_a3():
    assert 0 == 0


@pytest.mark.xfail(reason = "known issue")
def test_xfail():
    l = ['a','b']
    assert l[1]