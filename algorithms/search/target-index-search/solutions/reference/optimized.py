from typing import List


class BinarySearchTargetIndexFinder:
    """Binary search to locate target index in a sorted array."""

    def target_index_search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
