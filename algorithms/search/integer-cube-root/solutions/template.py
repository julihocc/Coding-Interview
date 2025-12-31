"""TEMPLATE: Integer Cube Root Solution

Implement a class whose name reflects the strategy (e.g., BinarySearchCubeRootFinder).
Judges instantiate the class and call its `integerCubeRoot` method directly.

Reference: See ../README.md for full problem description
"""

from abc import ABC, abstractmethod


class IntegerCubeRootBase(ABC):
    """Abstract base defining the required interface."""

    @abstractmethod
    def integerCubeRoot(self, n: int) -> int:
        """Return the largest integer k such that k^3 <= n."""
        raise NotImplementedError


class YourCubeRootFinder(IntegerCubeRootBase):
    """Rename and implement this class to match your approach."""

    def integerCubeRoot(self, n: int) -> int:
        # TODO: implement your chosen strategy (e.g., binary search over k)
        raise NotImplementedError
