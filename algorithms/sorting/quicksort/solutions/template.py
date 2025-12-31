"""TEMPLATE: Quicksort Solution

Function Signature:
    def quicksort(nums: List[int]) -> List[int]:

Problem:
    Sort array in ascending order and return sorted copy.

Reference: See ../README.md for full problem description
"""

from typing import List


def _partition(arr: List[int], low: int, high: int) -> int:
    """
    Helper: partition array around a pivot.
    
    Time Complexity: O(n)
    """
    # TODO: Implement partition logic with random pivot selection
    pass


def _quicksort(arr: List[int], low: int, high: int) -> None:
    """
    Helper: recursively sort subarray in-place.
    """
    # TODO: Implement recursive quicksort
    pass


def quicksort(nums: List[int]) -> List[int]:
    """
    Sort array using in-place quicksort.
    
    APPROACH:
    [Describe your strategy]
    
    Time Complexity: O(?) average
    Space Complexity: O(?)
    """
    
    # STEP 1: Handle edge cases
    if len(nums) < 2:
        return nums
    
    # STEP 2: Sort in-place using helper
    # TODO: Call _quicksort on the entire array
    pass
    
    # STEP 3: Return sorted array
    return nums
