from typing import List


class BinarySearchFinder:
    """Binary search with left refinement to find the first occurrence."""

    def find_first_occurrence(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        result = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                result = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return result
