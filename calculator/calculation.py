from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide
from calculator.operations import add_operands, subtract_operands, multiply_operands, divide_operands


class CalcOperation:
    def __init__(self, operand1: Decimal, operand2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operation = operation
    
    @staticmethod    
    def create_operation(operand1: Decimal, operand2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        return CalcOperation(operand1, operand2, operation)

    def execute(self) -> Decimal:
        """Execute the stored operation and return the result."""
        return self.operation(self.operand1, self.operand2)

    def __repr__(self):
        """Return a user-friendly string representation of the operation."""
        return f"CalcOperation({self.operand1}, {self.operand2}, {self.operation.__name__})"