from typing import List


class Solution:
    """Binary search to locate target index in a sorted array."""

    def __init__(self, nums: List[int]):
        self.nums = nums

    def target_index_search(self, target: int) -> int:
        left, right = 0, len(self.nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.nums[mid] == target:
                return mid
            if self.nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
