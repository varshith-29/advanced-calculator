"""Tests for the Calculator class"""
from decimal import Decimal
import pytest
from calculator.calculator import Calculator
from calculator.calculations import Calculations

@pytest.fixture(autouse=True)
def setup_calculator():
    """Clear calculation history before each test"""
    Calculations.clear_history()

@pytest.mark.parametrize("first_number, second_number, expected", [
    (Decimal('10'), Decimal('5'), Decimal('15')),
    (Decimal('-10'), Decimal('5'), Decimal('-5')),
    (Decimal('0'), Decimal('5'), Decimal('5')),
    (Decimal('0.1'), Decimal('0.2'), Decimal('0.3')),
])
def test_add(first_number, second_number, expected):
    """Test addition operation"""
    assert Calculator.add(first_number, second_number) == expected

@pytest.mark.parametrize("first_number, second_number, expected", [
    (Decimal('10'), Decimal('5'), Decimal('5')),
    (Decimal('-10'), Decimal('5'), Decimal('-15')),
    (Decimal('0'), Decimal('5'), Decimal('-5')),
    (Decimal('0.3'), Decimal('0.1'), Decimal('0.2')),
])
def test_subtract(first_number, second_number, expected):
    """Test subtraction operation"""
    assert Calculator.subtract(first_number, second_number) == expected

@pytest.mark.parametrize("first_number, second_number, expected", [
    (Decimal('10'), Decimal('5'), Decimal('50')),
    (Decimal('-10'), Decimal('5'), Decimal('-50')),
    (Decimal('0'), Decimal('5'), Decimal('0')),
    (Decimal('0.1'), Decimal('0.2'), Decimal('0.02')),
])
def test_multiply(first_number, second_number, expected):
    """Test multiplication operation"""
    assert Calculator.multiply(first_number, second_number) == expected

@pytest.mark.parametrize("first_number, second_number, expected", [
    (Decimal('10'), Decimal('5'), Decimal('2')),
    (Decimal('-10'), Decimal('5'), Decimal('-2')),
    (Decimal('0'), Decimal('5'), Decimal('0')),
    (Decimal('0.2'), Decimal('0.1'), Decimal('2')),
])
def test_divide(first_number, second_number, expected):
    """Test division operation"""
    assert Calculator.divide(first_number, second_number) == expected

def test_divide_by_zero():
    """Test division by zero raises error"""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(Decimal('10'), Decimal('0'))
        