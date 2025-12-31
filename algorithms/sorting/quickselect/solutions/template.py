"""TEMPLATE: Quickselect Solution

Function Signature:
    def quickselect(nums: List[int], k: int) -> int:

Problem:
    Find the k-th smallest element (0-indexed) in unsorted array.
    
Reference: See ../README.md for full problem description
"""

from typing import List


def _partition(arr: List[int], left: int, right: int, pivot_index: int) -> int:
    """
    Helper: partition array around pivot.
    Move pivot to final sorted position and return that position.
    
    Time Complexity: O(n)
    """
    # TODO: Implement partition logic
    # Swap pivot to end, then partition around it
    pass


def quickselect(nums: List[int], k: int) -> int:
    """
    Find k-th smallest element using quickselect.
    
    APPROACH:
    [Describe your strategy using partition]
    
    Time Complexity: O(?) average
    Space Complexity: O(?)
    """
    
    # STEP 1: Input validation
    if not nums:
        raise ValueError("nums must be non-empty")
    assert 0 <= k < len(nums), "k must be valid index"
    
    # STEP 2: Initialize search bounds
    left, right = 0, len(nums) - 1
    
    # STEP 3: Quickselect loop
    # TODO: Partition and recursively search relevant half
    # Check if pivot_index == k, pivot_index < k, or pivot_index > k
    pass
