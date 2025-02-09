from decimal import Decimal
from typing import Callable, List

from calculator.calculation import Calculation

class CalculationHistory:
    history_list: List[Calculation] = []

    @classmethod
    def record_calculation(cls, calc: Calculation):
        """Record a new calculation in the history."""
        cls.history_list.append(calc)

    @classmethod
    def get_all_history(cls) -> List[Calculation]:
        """Retrieve all past calculations from the history."""
        return cls.history_list

    @classmethod
    def reset_history(cls):
        """Clear all records from the calculation history."""
        cls.history_list.clear()

    @classmethod
    def get_most_recent(cls) -> Calculation:
        """Retrieve the most recent calculation. Returns None if the history is empty."""
        if cls.history_list:
            return cls.history_list[-1]
        return None

    @classmethod
    def search_by_operation(cls, operation: str) -> List[Calculation]:
        """Search and return a list of calculations matching the given operation name."""
        return [calc for calc in cls.history_list if calc.operation.__name__ == operation]