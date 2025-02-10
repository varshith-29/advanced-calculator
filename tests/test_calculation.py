from decimal import Decimal
import pytest
from calculator.calculation import CalcOperation
from calculator.operations import add_operands, subtract_operands, multiply_operands, divide_operands

@pytest.mark.parametrize("operand1, operand2, operation, expected_result", [
    (Decimal('20'), Decimal('4'), add_operands, Decimal('24')),
    (Decimal('20'), Decimal('4'), subtract_operands, Decimal('16')),
    (Decimal('20'), Decimal('4'), multiply_operands, Decimal('80')),
    (Decimal('20'), Decimal('4'), divide_operands, Decimal('5')),
    (Decimal('15.5'), Decimal('1.5'), add_operands, Decimal('17.0')),
    (Decimal('15.5'), Decimal('1.5'), subtract_operands, Decimal('14.0')),
    (Decimal('15.5'), Decimal('3'), multiply_operands, Decimal('46.5')),
    (Decimal('20'), Decimal('4'), divide_operands, Decimal('5')),
])
def test_arithmetic_operations(operand1, operand2, operation, expected_result):
    operation_instance = CalcOperation(operand1, operand2, operation)
    assert operation_instance.execute() == expected_result

def test_calculation_repr():
    operation_instance = CalcOperation(Decimal('20'), Decimal('4'), add_operands)
    expected_string = "CalcOperation(20, 4, add_operands)"
    assert operation_instance.__repr__() == expected_string

def test_division_by_zero():
    operation_instance = CalcOperation(Decimal('20'), Decimal('0'), divide_operands)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        operation_instance.execute()