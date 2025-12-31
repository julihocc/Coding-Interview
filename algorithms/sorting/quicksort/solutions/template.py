"""TEMPLATE: Quicksort Solution

Implement a class whose name reflects the strategy (e.g., InPlaceRandomizedQuicksort).
Judges instantiate the class and call its `quicksort` method directly.

Reference: See ../README.md for full problem description
"""

from abc import ABC, abstractmethod
from typing import List


class QuicksortBase(ABC):
    """Abstract base defining the required interface."""

    @abstractmethod
    def quicksort(self, nums: List[int]) -> List[int]:
        """Return a sorted list."""
        raise NotImplementedError


class YourQuicksort(QuicksortBase):
    """Rename and implement this class to match your approach."""

    def quicksort(self, nums: List[int]) -> List[int]:
        # TODO: implement your quicksort strategy
        raise NotImplementedError
