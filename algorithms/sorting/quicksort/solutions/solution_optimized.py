import random
from typing import List


class InPlaceRandomizedQuicksort:
    """In-place quicksort with randomized pivots."""

    def __init__(self, nums: List[int]):
        self.nums = nums

    def quicksort(self) -> List[int]:
        if len(self.nums) < 2:
            return self.nums

        self._quicksort(0, len(self.nums) - 1)
        return self.nums

    def _quicksort(self, low: int, high: int) -> None:
        if low < high:
            pivot_pos = self._partition(low, high)
            self._quicksort(low, pivot_pos - 1)
            self._quicksort(pivot_pos + 1, high)

    def _partition(self, low: int, high: int) -> int:
        pivot_index = random.randint(low, high)
        self.nums[pivot_index], self.nums[high] = self.nums[high], self.nums[pivot_index]
        pivot = self.nums[high]
        i = low

        for j in range(low, high):
            if self.nums[j] <= pivot:
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
                i += 1

        self.nums[i], self.nums[high] = self.nums[high], self.nums[i]
        return i
