import random
from typing import List


class RandomizedQuickselect:
    """Average-case linear-time quickselect with randomized pivots."""

    def quickselect(self, nums: List[int], k: int) -> int:
        if not nums:
            raise ValueError("nums must be non-empty")

        left, right = 0, len(nums) - 1

        while True:
            if left == right:
                return nums[left]

            pivot_index = random.randint(left, right)
            pivot_index = self._partition(nums, left, right, pivot_index)

            if pivot_index == k:
                return nums[pivot_index]
            if pivot_index < k:
                left = pivot_index + 1
            else:
                right = pivot_index - 1

    def _partition(self, arr: List[int], left: int, right: int, pivot_index: int) -> int:
        pivot_value = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left

        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1

        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index
