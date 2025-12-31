from typing import List


class BinarySearchFinder:
    """Binary search with left refinement to find the first occurrence."""

    def __init__(self, nums: List[int]):
        self.nums = nums

    def find_first_occurrence(self, target: int) -> int:
        low, high = 0, len(self.nums) - 1
        result = -1

        while low <= high:
            mid = (low + high) // 2
            if self.nums[mid] == target:
                result = mid
                high = mid - 1
            elif self.nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return result
