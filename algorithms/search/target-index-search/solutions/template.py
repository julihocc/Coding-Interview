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
    [Describe your strategy here]
    
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    
    # STEP 1: Input validation
    if not nums:
        return -1
    
    # STEP 2: Initialize binary search pointers
    left, right = 0, len(nums) - 1
    
    # STEP 3: Binary search loop
    # TODO: Implement search logic
    pass
    
    # STEP 4: Return result
    return -1
