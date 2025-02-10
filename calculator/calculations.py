from typing import List
from .calculation import Calculation

class Calculations:
    """Manages the history of calculations"""
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        """Adds a calculation to history"""
        cls.history.append(calculation)

    @classmethod
    def get_latest(cls) -> Calculation:
        """Returns the most recent calculation"""
        if not cls.history:
            raise ValueError("No calculations in history")
        return cls.history[-1]

    @classmethod
    def clear_history(cls) -> None:
        """Clears the calculation history"""
        cls.history.clear()

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Returns the full calculation history"""
        return cls.history.copy()
    