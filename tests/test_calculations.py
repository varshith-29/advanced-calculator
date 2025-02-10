"""Tests for the Calculations class"""
from decimal import Decimal
import pytest
from calculator.calculations import Calculations
from calculator.calculation import Calculation
from calculator.operations import add, subtract

@pytest.fixture(name="calc_history")
def setup_calculation_history():
    """Set up calculations for testing"""
    Calculations.clear_history()
    calculations = [
        Calculation(Decimal('10'), Decimal('5'), add),
        Calculation(Decimal('20'), Decimal('3'), subtract)
    ]
    for calc in calculations:
        Calculations.add_calculation(calc)
    return calculations

def test_add_calculation():
    """Test adding calculations to history"""
    Calculations.clear_history()
    calc = Calculation(Decimal('5'), Decimal('5'), add)
    Calculations.add_calculation(calc)
    assert len(Calculations.history) == 1
    assert Calculations.history[-1] == calc

def test_get_latest(calc_history):
    """Test getting the latest calculation"""
    latest = Calculations.get_latest()
    assert latest == calc_history[-1]
    assert latest.operation(latest.a, latest.b) == subtract(latest.a, latest.b)

def test_get_latest_empty():
    """Test getting latest calculation with empty history"""
    Calculations.clear_history()
    with pytest.raises(ValueError):
        Calculations.get_latest()

def test_clear_history():
    """Test clearing calculation history"""
    Calculations.add_calculation(Calculation(Decimal('5'), Decimal('5'), add))
    Calculations.clear_history()
    assert len(Calculations.history) == 0

def test_get_history(calc_history):
    """Test getting calculation history"""
    history = Calculations.get_history()
    assert len(history) == len(calc_history)
    assert history == calc_history
    history.append(Calculation(Decimal('1'), Decimal('1'), add))
    assert len(Calculations.history) == len(calc_history)
    