"""TEMPLATE: Class-based solution for Quickselect

Implement a class whose name reflects the strategy (e.g., RandomizedQuickselect).
Judges instantiate your class with nums in __init__ and call the method.

Reference: See ../README.md for full problem description
"""

from typing import List
import random

class YourQuickselect:
    """Rename and implement this class to match your approach.
    
    Example strategies: SortThenPickSelector, RandomizedQuickselect
    """

    def __init__(self, nums: List[int]):
        """Initialize with the array to select from.
        
        Args:
            nums: An unsorted list of integers.
        """
        self.nums = nums
        print(f"Initialized with nums: {self.nums}")

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
        
        left, right = 0, len(self.nums)-1
        pivot_index = left 

        while left <= right:
            pivot_index = random.randint(left, right)
            pivot_index = self._partition(left, right, pivot_index)
            print(f"pivot_index: {pivot_index}")

            if pivot_index==k:
                return self.nums[pivot_index]
            if pivot_index < k:
                left += 1
            if pivot_index > k:
                right -= 1

    
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
        wall = left
        pivot_value = self.nums[pivot_index]
        self._swap(pivot_index, right)

        for index in range(left, right):
            if self.nums[index] < pivot_value:
                self._swap(index, wall)
                wall += 1
        
        self._swap(wall, right)

        return wall

    
    def _swap(self, i: int, j: int) -> None:
        """Swap two elements in self.nums by their indices.
        
        Args:
            i: First index.
            j: Second index.
        """
        # TODO: Exchange self.nums[i] and self.nums[j]
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

if __name__ == "__main__":
    # Simple sanity check
    selector = YourQuickselect([3, 1, 2, 7, 5, 4, 6])
    print(selector.quickselect(0))  # Expected: 1
    print(selector.quickselect(1))  # Expected: 2
    print(selector.quickselect(2))  # Expected: 3
    print(selector.quickselect(3))  # Expected: 4
    print(selector.quickselect(4))  # Expected: 5   



