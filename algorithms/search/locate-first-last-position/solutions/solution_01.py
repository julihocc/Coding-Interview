"""TEMPLATE: Class-based solution for Locate First and Last Position

Reference: See ../README.md for full problem description
"""

class Solution:
    def binary_search(self, nums, target, left, right, find_first):
        index = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                index = mid
                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return index

    def search_range(self, nums: list[int], target: int) -> list[int]:
        """Find the starting and ending position of a given target value.

        Args:
            nums: A list of integers sorted in non-decreasing order.
            target: The integer value to search for.

        Returns:
            A list of two integers [start, end], or [-1, -1] if not found.
        """
        first = self.binary_search(nums, target, 0, len(nums) - 1, True)
        last = self.binary_search(nums, target, 0, len(nums) - 1, False)
        return [first, last]
