"""TEMPLATE: Class-based solution for Quicksort

Implement a class whose name reflects the strategy (e.g., InPlaceRandomizedQuicksort).
Judges instantiate your class with nums in __init__ and call the method.

Reference: See ../README.md for full problem description
"""

from typing import List


class YourQuicksort:
    """Rename and implement this class to match your approach.
    
    Example strategies: BuiltinSorter, InPlaceRandomizedQuicksort
    """

    def __init__(self, nums: List[int]):
        """Initialize with the array to sort.
        
        Args:
            nums: An unsorted list of integers.
        """
        self.nums = nums

    def quicksort(self) -> List[int]:
        """Sort self.nums in-place and return the sorted array.
        
        Expected behavior:
        - Modify self.nums so elements are in ascending order
        - Return the sorted self.nums (same object, now sorted)
        - Handle edge cases: empty, single element, duplicates
        
        Hint: Use divide-and-conquer with _quicksort recursive helper.
              Use _partition to split array around a pivot.
        
        Returns:
            The sorted self.nums array.
        """
        # TODO: Implement sort strategy
        # Consider: Built-in sort vs. Quicksort with partitioning
        # For quicksort: call _quicksort on initial range [0, len(nums)-1]
        raise NotImplementedError
    
    def _quicksort(self, low: int, high: int) -> None:
        """Recursively sort the range [low, high] in self.nums.
        
        Divide-and-conquer approach:
        1. Partition to find pivot position
        2. Recursively sort left and right subarrays
        
        Args:
            low: Left boundary of range to sort.
            high: Right boundary of range to sort.
        """
        # TODO: Implement recursive sorting
        # Base case: if low >= high, range is sorted
        # Recursive case: partition, then sort left and right
        raise NotImplementedError
    
    def _partition(self, low: int, high: int) -> int:
        """Partition array around a pivot and return its final position.
        
        Move pivot to partition position such that:
        - All elements <= pivot are to the left
        - All elements > pivot are to the right
        
        Args:
            low: Left boundary of partition range.
            high: Right boundary of partition range.
            
        Returns:
            The final position of the pivot after partitioning.
        """
        pivot = self.nums[high]
        i = low - 1
        
        for j in range(low, high):
            if self.nums[j] <= pivot:
                i += 1
                self._swap(i, j)
                
        self._swap(i + 1, high)
        return i + 1
    
    def _swap(self, i: int, j: int) -> None:
        """Swap two elements in self.nums by their indices.
        
        Args:
            i: First index.
            j: Second index.
        """
        # TODO: Exchange self.nums[i] and self.nums[j]
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
