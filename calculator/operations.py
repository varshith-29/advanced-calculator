from decimal import Decimal

def add_operands(operand1: Decimal, operand2: Decimal) -> Decimal:
    """Return the sum of two operands."""
    return operand1 + operand2

def subtract_operands(operand1: Decimal, operand2: Decimal) -> Decimal:
    """Return the difference between two operands."""
    return operand1 - operand2

def multiply_operands(operand1: Decimal, operand2: Decimal) -> Decimal:
    """Return the product of two operands."""
    return operand1 * operand2

def divide_operands(operand1: Decimal, operand2: Decimal) -> Decimal:
    """Return the quotient of two operands, raises an error if dividing by zero."""
    if operand2 == 0:
        raise ValueError("Cannot divide by zero")
    return operand1 / operand2
