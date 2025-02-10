"""Tests for the operations module"""
from decimal import Decimal
import pytest
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("operation, first_number, second_number, expected", [
    (add, Decimal('10'), Decimal('5'), Decimal('15')),
    (add, Decimal('-10'), Decimal('5'), Decimal('-5')),
    (subtract, Decimal('10'), Decimal('5'), Decimal('5')),
    (subtract, Decimal('-10'), Decimal('5'), Decimal('-15')),
    (multiply, Decimal('10'), Decimal('5'), Decimal('50')),
    (multiply, Decimal('-10'), Decimal('5'), Decimal('-50')),
    (divide, Decimal('10'), Decimal('5'), Decimal('2')),
    (divide, Decimal('-10'), Decimal('5'), Decimal('-2')),
])
def test_operations(operation, first_number, second_number, expected):
    """Test all basic operations"""
    assert operation(first_number, second_number) == expected

def test_divide_by_zero():
    """Test division by zero raises error"""
    with pytest.raises(ZeroDivisionError):
        divide(Decimal('10'), Decimal('0'))
        