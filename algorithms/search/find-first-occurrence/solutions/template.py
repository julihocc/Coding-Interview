"""TEMPLATE: Find First Occurrence Solution

Function Signature:
    def find_first_occurrence(nums: List[int], target: int) -> int:

Problem:
    Find the first (leftmost) occurrence of target in sorted array.
    Return -1 if not found.

Reference: See ../README.md for full problem description
"""

from typing import List


def find_first_occurrence(nums: List[int], target: int) -> int:
    """
    Find the first occurrence of target using binary search.
    
    APPROACH:
    Binary search to find target, then continue searching left to find first occurrence.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    
    # STEP 1: Input validation
    if not nums:
        return -1
    
    # STEP 2: Initialize binary search pointers
    low, high = 0, len(nums) - 1
    result = -1
    
    # STEP 3: Binary search
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            result = mid
            # Continue searching in left half for first occurrence
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    # STEP 4: Return result
    return result
