from typing import List


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        """
        Finds the insert position of a target element in a sorted array using linear scan.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
                
        return len(nums)
