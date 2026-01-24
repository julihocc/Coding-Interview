from typing import List


class Solution:
    def search_range(self, nums: List[int], target: int) -> List[int]:
        """
        Finds the first and last position of a target element in a sorted array using binary search.
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        
        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            first_occurrence = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first_occurrence = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first_occurrence

        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            last_occurrence = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    last_occurrence = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last_occurrence

        first = find_first(nums, target)
        if first == -1:
            return [-1, -1]
        
        last = find_last(nums, target)
        return [first, last]
