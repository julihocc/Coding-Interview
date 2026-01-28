import random
from typing import List


class Solution:
    """In-place quicksort using an explicit stack (Iterative), sorting in descending order."""

    def __init__(self, nums: List[int]):
        self.nums = nums

    def quicksort(self) -> List[int]:
        if len(self.nums) < 2:
            return self.nums

        stack = [(0, len(self.nums) - 1)]
        
        while stack:
            low, high = stack.pop()
            
            if low < high:
                pivot_pos = self._partition(low, high)
                
                # Push ranges to stack.
                if pivot_pos - 1 > low:
                    stack.append((low, pivot_pos - 1))
                if pivot_pos + 1 < high:
                    stack.append((pivot_pos + 1, high))
                    
        return self.nums

    def _partition(self, low: int, high: int) -> int:
        pivot_index = random.randint(low, high)
        self.nums[pivot_index], self.nums[high] = self.nums[high], self.nums[pivot_index]
        pivot = self.nums[high]
        i = low

        for j in range(low, high):
            # Change comparison to >= for descending order
            if self.nums[j] >= pivot:
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
                i += 1

        self.nums[i], self.nums[high] = self.nums[high], self.nums[i]
        return i
