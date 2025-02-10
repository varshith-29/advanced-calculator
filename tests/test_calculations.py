from decimal import Decimal
import pytest # type: ignore
from calculator.calculation import CalcOperation
from calculator.calculations import CalculationHistory
from calculator.operations import add_operands, subtract_operands

@pytest.fixture
def prepare_calculations():
    CalculationHistory.reset_history()
    CalculationHistory.record_calculation(CalcOperation(Decimal('10'), Decimal('5'), add_operands))
    CalculationHistory.record_calculation(CalcOperation(Decimal('20'), Decimal('3'), subtract_operands))

def test_add_to_history(prepare_calculations):
    calc = CalcOperation(Decimal('2'), Decimal('2'), add_operands)
    CalculationHistory.record_calculation(calc)
    assert CalculationHistory.get_most_recent() == calc

def test_fetch_history(prepare_calculations):
    history = CalculationHistory.get_all_history()
    assert len(history) == 2

def test_reset_history(prepare_calculations):
    CalculationHistory.reset_history()
    assert len(CalculationHistory.get_all_history()) == 0

def test_latest_calculation(prepare_calculations):
    latest = CalculationHistory.get_most_recent()
    assert latest.operand1 == Decimal('20') and latest.operand2 == Decimal('3')

def test_find_calculations_by_operation(prepare_calculations):
    add_ops = CalculationHistory.find_by_operation("add")
    assert len(add_ops) == 1
    subtract_ops = CalculationHistory.find_by_operation("subtract")
    assert len(subtract_ops) == 1

def test_latest_with_empty_history():
    CalculationHistory.reset_history()
    assert CalculationHistory.get_most_recent() is None