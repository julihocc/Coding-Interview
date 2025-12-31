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
    [Describe your strategy here - e.g., Binary search + left refinement]
    
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    
    # STEP 1: Input validation
    if not nums:
        return -1
    
    # STEP 2: Initialize binary search pointers
    low, high = 0, len(nums) - 1
    result = -1
    
    # STEP 3: Binary search loop
    # TODO: Implement search logic
    # When target is found, continue searching left for first occurrence
    pass
    
    # STEP 4: Return result
    return result
