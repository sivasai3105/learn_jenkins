import pytest
import sys

pytest_mark = pytest.mark.skipif(sys.platform == "win32", reason="will run only on linux")


class TestMyStuff:
    @pytest.mark.skip(reason="Skipping for no reason specified")
    def test_type(self):
        assert type(1) == int

    @pytest.mark.skipif(sys.version_info > (3, 6), reason="doesn't work for version > 3.6")
    def test_case(self):
        assert str.lower("Python") == "python"

    def test_case01(self):
        with pytest.raises(ZeroDivisionError):
            assert (1 / 0)

    def func(self):
        raise ValueError("Exception func raised")

    def test_case02(self):
        with pytest.raises(Exception) as e:
            self.func()
        print(f" Exception is --> {e}")
        assert (str(e.value)) == "Exception func raised"


def fun2():
    return 5


@pytest.mark.skipif(fun2() == 5 and pytest.__version__ == "50.5.0", reason="skipping as this returns 5")
def test_case03():
    assert fun2() == 5
