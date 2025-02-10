# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
from typing import Callable, Any

class Calculation:
    """Handles individual calculations"""
    
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> None:
        self.a = a
        self.b = b
        self.operation = operation
        self._result: Decimal | None = None

    @classmethod
    def create(cls, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> 'Calculation':
        """Factory method to create a new calculation"""
        return cls(a, b, operation)

    def perform(self) -> Decimal:
        """Executes the calculation and stores the result"""
        self._result = self.operation(self.a, self.b)
        return self._result

    @property
    def result(self) -> Decimal:
        """Returns the calculation result"""
        if self._result is None:
            self.perform()
        return self._result
    