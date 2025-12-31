"""TEMPLATE: Target Index Search Solution

Implement a class whose name reflects the strategy (e.g., BinarySearchTargetIndexFinder).
Judges instantiate the class and call its `target_index_search` method directly.

Reference: See ../README.md for full problem description
"""

from abc import ABC, abstractmethod
from typing import List


class TargetIndexSearchBase(ABC):
    """Abstract base defining the required interface."""

    @abstractmethod
    def target_index_search(self, nums: List[int], target: int) -> int:
        """Return the index of target in sorted nums, or -1 if absent."""
        raise NotImplementedError


class YourTargetIndexFinder(TargetIndexSearchBase):
    """Rename and implement this class to match your approach."""

    def target_index_search(self, nums: List[int], target: int) -> int:
        # TODO: implement your search strategy (e.g., binary search)
        raise NotImplementedError
