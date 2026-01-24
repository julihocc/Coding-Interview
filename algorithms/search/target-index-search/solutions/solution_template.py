"""TEMPLATE: Class-based solution for Target Index Search

Implement a class whose name reflects the strategy (e.g., BinarySearchTargetIndexFinder).
Judges instantiate your class with nums in __init__ and call the method.

Reference: See ../README.md for full problem description
"""

from typing import List


class YourTargetIndexFinder:
    """Rename and implement this class to match your approach.
    
    Example strategies: LinearTargetIndexFinder, BinarySearchTargetIndexFinder
    """

    def __init__(self, nums: List[int]):
        """Initialize with the sorted array to search in.
        
        Args:
            nums: A sorted list of integers to search within.
        """
        self.nums = nums

    def target_index_search(self, target: int) -> int:
        """Find the index of target in a sorted array.
        
        Expected behavior:
        - Return the index where self.nums[index] == target
        - Return -1 if target is not found
        - For sorted arrays, binary search is more efficient than linear scan
        
        Args:
            target: The value to search for.
            
        Returns:
            The index of the target, or -1 if not found.
        """
        # TODO: Implement search strategy
        # Consider: Linear scan vs. Binary search
        # For binary search, adjust left/right pointers based on comparison
        raise NotImplementedError
