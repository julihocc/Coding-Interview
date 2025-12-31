"""TEMPLATE: Target Index Search Solution

Function Signature:
    def target_index_search(nums: List[int], target: int) -> int:

Problem:
    Find the index of target in sorted array.
    Return -1 if not found.

Reference: See ../README.md for full problem description
"""

from typing import List


def target_index_search(nums: List[int], target: int) -> int:
    """
    Find target using binary search.
    
    APPROACH:
    Classic binary search on sorted array.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    
    # STEP 1: Input validation
    if not nums:
        return -1
    
    # STEP 2: Initialize binary search pointers
    left, right = 0, len(nums) - 1
    
    # STEP 3: Binary search loop
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # STEP 4: Return result
    return -1
