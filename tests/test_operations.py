from decimal import Decimal
import pytest # type: ignore
from calculator.calculation import CalcOperation
from calculator.operations import add_operands, subtract_operands, multiply_operands, divide_operands

def test_addition_operation():
    calc = CalcOperation(Decimal('25'), Decimal('10'), add_operands)
    assert calc.execute() == Decimal('35')

def test_subtraction_operation():
    calc = CalcOperation(Decimal('25'), Decimal('10'), subtract_operands)
    assert calc.execute() == Decimal('15')

def test_multiplication_operation():
    calc = CalcOperation(Decimal('25'), Decimal('5'), multiply_operands)
    assert calc.execute() == Decimal('125')

def test_division_operation():
    calc = CalcOperation(Decimal('25'), Decimal('5'), divide_operands)
    assert calc.execute() == Decimal('5')

def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc = CalcOperation(Decimal('25'), Decimal('0'), divide_operands)
        calc.execute()