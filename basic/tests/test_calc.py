from src.calc import add, subtract, multiply, divide

def test_add():
    assert add(3,3) == 6
    assert add(3, -1) == 2
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(3,1) == 2
    assert subtract(3, -1) == 4
    assert subtract(-1, -1) == 0


def test_multiply():
    assert multiply(3, 3) == 9
    assert multiply(3, -1) == -3
    assert multiply(-1, -1) == 1


def test_divide():
    assert divide(4, 2) == 2
    assert divide(4, 4) == 1