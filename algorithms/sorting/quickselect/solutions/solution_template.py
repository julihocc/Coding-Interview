"""TEMPLATE: Class-based solution for Quickselect

Implement a class whose name reflects the strategy (e.g., RandomizedQuickselect).
Judges instantiate your class with nums in __init__ and call the method.

Reference: See ../README.md for full problem description
"""

from typing import List


class Solution:
    """Rename and implement this class to match your approach.
    
    Example strategies: SortThenPickSelector, RandomizedQuickselect
    """

    def __init__(self, nums: List[int]):
        """Initialize with the array to select from.
        
        Args:
            nums: An unsorted list of integers.
        """
        self.nums = nums

    def quickselect(self, k: int) -> int:
        """Find and return the k-th smallest element (0-indexed).
        
        Expected behavior:
        - Return the element at position k when sorted in ascending order
        - For [3, 1, 2], k=0 returns 1, k=1 returns 2, k=2 returns 3
        - Modifies self.nums in-place during selection (if using partitioning)
        
        Hint: Use _partition helper to split around a pivot element.
              Compare partition result with k to narrow search range.
        
        Args:
            k: The index of the smallest element to find (0-indexed).
            
        Returns:
            The k-th smallest element in the array.
        """
        # TODO: Implement selection strategy
        # Consider: Sort-then-pick vs. Quickselect with partitioning
        # For quickselect: use binary search on left/right with _partition
        raise NotImplementedError
    
    def _partition(self, left: int, right: int, pivot_index: int) -> int:
        """Partition array around a pivot and return its final position.
        
        Move pivot to partition position such that:
        - All elements < pivot are to the left
        - All elements >= pivot are to the right
        
        This allows binary search by comparing final position with target k.
        
        Args:
            left: Left boundary of partition range.
            right: Right boundary of partition range.
            pivot_index: Initial index of the pivot element.
            
        Returns:
            The final position of the pivot after partitioning.
        """
        # TODO: Implement partitioning logic
        # 1. Swap pivot to right boundary (use _swap helper)
        # 2. Iterate left to right, moving smaller elements left
        # 3. Swap pivot to final position
        # 4. Return final position
        raise NotImplementedError
    
    def _swap(self, i: int, j: int) -> None:
        """Swap two elements in self.nums by their indices.
        
        Args:
            i: First index.
            j: Second index.
        """
        # TODO: Exchange self.nums[i] and self.nums[j]
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
