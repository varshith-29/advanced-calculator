from calculator.calculations import Calculations # type: ignore
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation
from decimal import Decimal
from typing import Callable

class ArithmeticCalculator:
    @staticmethod
    def _execute_operation(operand1: Decimal, operand2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calculation = Calculation.create(operand1, operand2, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add_numbers(operand1: Decimal, operand2: Decimal) -> Decimal:
        return ArithmeticCalculator._execute_operation(operand1, operand2, add)

    @staticmethod
    def subtract_numbers(operand1: Decimal, operand2: Decimal) -> Decimal:
        return ArithmeticCalculator._execute_operation(operand1, operand2, subtract)

    @staticmethod
    def multiply_numbers(operand1: Decimal, operand2: Decimal) -> Decimal:
        return ArithmeticCalculator._execute_operation(operand1, operand2, multiply)

    @staticmethod
    def divide_numbers(operand1: Decimal, operand2: Decimal) -> Decimal:
        return ArithmeticCalculator._execute_operation(operand1, operand2, divide)