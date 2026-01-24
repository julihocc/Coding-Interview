from typing import List


class Solution:
    """Sort then pick the k-th element."""

    def __init__(self, nums: List[int]):
        self.nums = nums

    def quickselect(self, k: int) -> int:
        sorted_nums = sorted(self.nums)
        return sorted_nums[k]
