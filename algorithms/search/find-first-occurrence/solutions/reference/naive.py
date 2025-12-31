from typing import List


class LinearScanFinder:
    """Linear scan approach to locate the first occurrence."""

    def __init__(self, nums: List[int]):
        self.nums = nums

    def find_first_occurrence(self, target: int) -> int:
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                return i
        return -1
