"""TEMPLATE: Find Crossover Indices Solution

Implement a class whose name reflects the strategy (e.g., BinarySearchCrossoverFinder).
Judges instantiate the class and call its `findCrossoverIndex` method directly.

Reference: See ../README.md for full problem description
"""

from abc import ABC, abstractmethod


class FindCrossoverBase(ABC):
    """Abstract base defining the required interface."""

    @abstractmethod
    def findCrossoverIndex(self, x, y):
        """Return the crossover index or -1 if none exists."""
        raise NotImplementedError


class YourCrossoverFinder(FindCrossoverBase):
    """Rename and implement this class to match your approach."""

    def findCrossoverIndex(self, x, y):
        # TODO: implement your strategy (e.g., binary search over crossover)
        raise NotImplementedError
