"""TEMPLATE: Class-based solution for Find First Occurrence

Implement a class whose name conveys the strategy (e.g., BinarySearchFinder,
TwoPointerFinder). Judges will instantiate your class and call its
`find_first_occurrence` method directly—no standalone solve() wrapper.

Reference: See ../README.md for full problem description
"""

from abc import ABC, abstractmethod
from typing import List


class FindFirstOccurrenceBase(ABC):
    """Abstract base defining the required interface."""

    @abstractmethod
    def find_first_occurrence(self, nums: List[int], target: int) -> int:
        """Return the leftmost index of target in sorted nums, or -1 if absent."""
        raise NotImplementedError


class YourStrategyFinder(FindFirstOccurrenceBase):
    """Rename this class to describe your approach and implement the method."""

    def find_first_occurrence(self, nums: List[int], target: int) -> int:
        # TODO: implement your chosen strategy (e.g., binary search)
        raise NotImplementedError
