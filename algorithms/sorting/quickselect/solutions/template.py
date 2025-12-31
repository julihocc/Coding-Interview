"""TEMPLATE: Quickselect Solution

Implement a class whose name reflects the strategy (e.g., RandomizedQuickselect).
Judges instantiate the class and call its `quickselect` method directly.

Reference: See ../README.md for full problem description
"""

from abc import ABC, abstractmethod
from typing import List


class QuickselectBase(ABC):
    """Abstract base defining the required interface."""

    @abstractmethod
    def quickselect(self, nums: List[int], k: int) -> int:
        """Return the k-th smallest element (0-indexed)."""
        raise NotImplementedError


class YourQuickselect(QuickselectBase):
    """Rename and implement this class to match your approach."""

    def quickselect(self, nums: List[int], k: int) -> int:
        # TODO: implement your quickselect strategy
        raise NotImplementedError
