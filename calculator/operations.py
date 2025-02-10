from decimal import Decimal
from typing import Callable

def add(a: Decimal, b: Decimal) -> Decimal:
    """Performs addition"""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Performs subtraction"""
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Performs multiplication"""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """Performs division"""
    if b == Decimal('0'):
        raise ZeroDivisionError("Division by zero is undefined")
    return a / b
