"""TEMPLATE: Class-based solution for Search Rotated Sorted Array

Reference: See ../README.md for full problem description
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Search for a target value in a rotated sorted array.

        Args:
            nums: A list of integers sorted in ascending order (with distinct values)
                  that is rotated at some pivot unknown to you beforehand.
            target: The integer value to search for.

        Returns:
            The index of target if it is in nums, or -1 if it is not in nums.
        """
        # TODO: Implement your solution here
        left, right = 0, len(nums)-1 

        while left <= right: 
            mid = (left+right)//2
            if nums[mid] == target: 
                return mid 
            # case: leftmost part is ordered
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1 
                else: 
                    left = mid+1 
            # case rightmost part is ordered:
            else:
                if nums[mid] < target <= nums[right]: 
                    left = mid+1 
                else: 
                    right = mid -1 
        
        return -1
