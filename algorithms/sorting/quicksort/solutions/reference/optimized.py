import random
from typing import List


class InPlaceRandomizedQuicksort:
    """In-place quicksort with randomized pivots."""

    def quicksort(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        self._quicksort(nums, 0, len(nums) - 1)
        return nums

    def _quicksort(self, arr: List[int], low: int, high: int) -> None:
        if low < high:
            pivot_pos = self._partition(arr, low, high)
            self._quicksort(arr, low, pivot_pos - 1)
            self._quicksort(arr, pivot_pos + 1, high)

    def _partition(self, arr: List[int], low: int, high: int) -> int:
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pivot = arr[high]
        i = low

        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[high] = arr[high], arr[i]
        return i
