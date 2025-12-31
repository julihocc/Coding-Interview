"""TEMPLATE: Multiway Merge Solution

Implement a class whose name reflects the strategy (e.g., PairwiseMergeKWay).
Judges instantiate the class and call its `kWayMerge` method directly.

Reference: See ../README.md for full problem description
"""

from abc import ABC, abstractmethod


class KWayMergeBase(ABC):
    """Abstract base defining the required interface."""

    @abstractmethod
    def kWayMerge(self, list_of_lists):
        """Return a single sorted list from sorted input lists."""
        raise NotImplementedError


class YourKWayMerger(KWayMergeBase):
    """Rename and implement this class to match your approach."""

    def kWayMerge(self, list_of_lists):
        # TODO: implement your merge strategy (e.g., pairwise merging, heap)
        raise NotImplementedError
