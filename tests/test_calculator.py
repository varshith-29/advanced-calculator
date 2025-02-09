from calculator import Calculator

def test_calculator_add():
    '''Test the add method of Calculator'''
    result = Calculator.add(2, 2)
    assert result == 4

def test_calculator_subtract():
    '''Test the subtract method of Calculator'''
    result = Calculator.subtract(5, 3)
    assert result == 2

def test_calculator_multiply():
    '''Test the multiply method of Calculator'''
    result = Calculator.multiply(3, 3)
    assert result == 9

def test_calculator_divide():
    '''Test the divide method of Calculator'''
    result = Calculator.divide(10, 2)
    assert result == 5