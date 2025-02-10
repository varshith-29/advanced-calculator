from decimal import Decimal
from typing import Callable
from .calculations import Calculations
from .calculation import Calculation
from .operations import add, subtract, multiply, divide

class Calculator:
    """Main calculator class providing the calculation interface"""

    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Creates and performs a calculation, then returns the result"""
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Performs addition"""
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Performs subtraction"""
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Performs multiplication"""
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Performs division"""
        return Calculator._perform_operation(a, b, divide)
    