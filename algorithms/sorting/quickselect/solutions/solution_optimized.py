import random
from typing import List


class Solution:
    """Average-case linear-time quickselect with randomized pivots."""

    def __init__(self, nums: List[int]):
        if not nums:
            raise ValueError("nums must be non-empty")
        self.nums = nums

    def quickselect(self, k: int) -> int:
        left, right = 0, len(self.nums) - 1

        while True:
            if left == right:
                return self.nums[left]

            pivot_index = random.randint(left, right)
            pivot_index = self._partition(left, right, pivot_index)

            if pivot_index == k:
                return self.nums[pivot_index]
            if pivot_index < k:
                left = pivot_index + 1
            else:
                right = pivot_index - 1

    def _partition(self, left: int, right: int, pivot_index: int) -> int:
        pivot_value = self.nums[pivot_index]
        self.nums[pivot_index], self.nums[right] = self.nums[right], self.nums[pivot_index]
        store_index = left

        for i in range(left, right):
            if self.nums[i] < pivot_value:
                self.nums[store_index], self.nums[i] = self.nums[i], self.nums[store_index]
                store_index += 1

        self.nums[right], self.nums[store_index] = self.nums[store_index], self.nums[right]
        return store_index
