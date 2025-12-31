from typing import List


class LinearScanFinder:
    """Linear scan approach to locate the first occurrence."""

    def find_first_occurrence(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
