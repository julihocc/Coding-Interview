"""TEMPLATE: Class-based solution for Quicksort

Implement a class whose name reflects the strategy (e.g., InPlaceRandomizedQuicksort).
Judges instantiate your class with nums in __init__ and call the method.

Reference: See ../README.md for full problem description
"""

from typing import List
import random


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
        print("Initialized with nums:", self.nums)

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
        self._quicksort(0, len(self.nums) - 1)
        return self.nums
    
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

        print("Quicksort called with low:", low, "high:", high)


        if low<=high:
            pivot_index = self._partition(low, high)
            self._quicksort(low, pivot_index-1)
            self._quicksort(pivot_index+1, high)

        

    
    def _partition(self, low_index: int, high_index: int) -> int:
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
        # TODO: Implement partitioning logic
        # 1. Select a pivot (first, last, or random)
        # 2. Move pivot to right boundary (use _swap helper)
        # 3. Iterate left to right, moving smaller elements left
        # 4. Swap pivot to final position
        # 5. Return final position

        print("Partition called with low:", low_index, "high:", high_index)

        pivot_index = random.randint(low_index, high_index)
        pivot_value = self.nums[pivot_index]
        stored_index = low_index 
        self._swap(pivot_index, high_index)

        for i in range(low_index, high_index):
            if self.nums[i] < pivot_value:
                self._swap(i, stored_index)
                stored_index+=1
        
        self._swap(stored_index, high_index)

        print(f"Array after partitioning: {self.nums}")
        print(f"Pivot {pivot_value} placed at index {stored_index}")

        return stored_index

    def _swap(self, i: int, j: int) -> None:
        """Swap two elements in self.nums by their indices.
        
        Args:
            i: First index.
            j: Second index.
        """
        # TODO: Exchange self.nums[i] and self.nums[j]
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

if __name__ == "__main__":
    # Example usage
    sorter = YourQuicksort([3, 6, 8, 10, 1, 2, 1])
    sorted_nums = sorter.quicksort()
    print("Sorted array:", sorted_nums)
