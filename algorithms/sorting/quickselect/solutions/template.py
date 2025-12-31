"""
TEMPLATE: Quickselect Solution

Function Signature:
    def quickselect(nums: List[int], k: int) -> int:

Problem:
    Find the k-th smallest element (0-indexed) in unsorted array.
    
Reference: See ../README.md for full problem description
"""

from typing import List


def quickselect(nums: List[int], k: int) -> int:
    """
    [FILL IN: Brief one-liner describing your approach]
    
    APPROACH:
    [Describe your strategy here - e.g., Sort & Index, Quickselect with Partition]
    
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    
    # STEP 1: Input validation
    assert nums, "Array must not be empty"
    assert 0 <= k < len(nums), "k must be valid index"
    
    # STEP 2: Handle edge cases
    if len(nums) == 1:
        return nums[0]
    
    # STEP 3: Initialize helper functions (if needed)
    # [Define partition, recursive select, etc.]
    
    # STEP 4: Main selection algorithm
    # [Implement your solution here]
    pass
    
    # STEP 5: Return k-th smallest element
    # [return element_at_k]
