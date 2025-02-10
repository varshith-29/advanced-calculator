# tests/test_calculation.py
"""Tests for the Calculation class"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("first_number, second_number, operation, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),
    (Decimal('10'), Decimal('5'), divide, Decimal('2')),
])
def test_calculation_operations(first_number, second_number, operation, expected):
    """Testing various calculation operations"""
    calculation = Calculation(first_number, second_number, operation)
    result = calculation.perform()
    assert result == expected
    assert calculation.result == expected

def test_calculation_create():
    """Test the create class method"""
    first_number, second_number = Decimal('10'), Decimal('5')
    calculation = Calculation.create(first_number, second_number, add)
    assert isinstance(calculation, Calculation)
    assert calculation.a == first_number
    assert calculation.b == second_number
    assert calculation.operation(first_number, second_number) == add(first_number, second_number)

def test_calculation_result_property():
    """Test the result property of calculation"""
    calculation = Calculation(Decimal('10'), Decimal('5'), add)
    assert calculation._result is None  # pylint: disable=protected-access
    result = calculation.result
    assert result == Decimal('15')
    assert calculation._result == Decimal('15')  # pylint: disable=protected-access
