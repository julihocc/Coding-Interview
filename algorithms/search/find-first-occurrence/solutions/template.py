"""TEMPLATE: Class-based solution for Find First Occurrence

Implement a class whose name conveys the strategy (e.g., BinarySearchFinder).
Judges instantiate your class with array data in __init__ and call the method.

Reference: See ../README.md for full problem description
"""

from typing import List


class YourStrategyFinder:
    """Rename and implement this class to match your approach.
    
    Example strategies: LinearScanFinder, BinarySearchFinder
    """

    def __init__(self, nums: List[int]):
        """Initialize with the sorted array to search in.
        
        Args:
            nums: A sorted list of integers to search within.
        """
        self.nums = nums

    def find_first_occurrence(self, target: int) -> int:
        """Find the index of the first occurrence of target in self.nums.
        
        Expected behavior:
        - Return the smallest index i where self.nums[i] == target
        - Return -1 if target is not found
        - For a sorted array with duplicates, return the leftmost occurrence
        
        Args:
            target: The value to search for.
            
        Returns:
            The index of the first occurrence, or -1 if not found.
        """
        # TODO: Implement search strategy
        # Consider: Linear scan vs. Binary search with left refinement
        raise NotImplementedError
