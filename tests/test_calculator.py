from calculator import add, subtract, multiply, divide

# test_add
def test_add():
    assert add(7, 3) == 10
    assert add(7) == 7
    assert add(5.2, 3.1) == 8.3
    assert add(-5, -3) == -8


# test_subtract
def test_subtract():
    assert subtract(7, 3) == 4
    assert subtract(7) == 7
    assert subtract(5.2, 3.1) == 2.1
    assert subtract(-5, -3) == -2


# test_multiply
def test_multiply():
    assert multiply(7, 3) == 21
    assert multiply(7) == 7
    assert multiply(5.2, 3.1) == 16.12
    assert multiply(-5, -3) == 15


# test_divide
def test_divide():
    assert divide(7, 3) == 2.3333333333333335
    assert divide(7) == 7
    assert divide(5.2, 3.1) == 1.6774193548387097
    assert divide(-5, -3) == 1.6666666666666667
    assert divide(5, 2) == 2.5
    try:
        divide(5, 0)
    except ValueError as e:
        assert str(e) == 'Can not divide by zero!'
    else:
        assert False