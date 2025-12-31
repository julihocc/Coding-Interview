"""TEMPLATE: Quicksort Solution

Function Signature:
    def quicksort(nums: List[int]) -> List[int]:

Problem:
    Sort array in ascending order and return sorted copy.

Reference: See ../README.md for full problem description
"""

import random
from typing import List


def _partition(arr: List[int], low: int, high: int) -> int:
    """
    Helper function: partition array around random pivot.
    
    Time Complexity: O(n)
    """
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low
    
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[i], arr[high] = arr[high], arr[i]
    return i


def _quicksort(arr: List[int], low: int, high: int) -> None:
    """
    Helper function: recursively sort subarray in-place.
    """
    if low < high:
        pivot_pos = _partition(arr, low, high)
        _quicksort(arr, low, pivot_pos - 1)
        _quicksort(arr, pivot_pos + 1, high)


def quicksort(nums: List[int]) -> List[int]:
    """
    Sort array using in-place quicksort with randomized pivots.
    
    APPROACH:
    Partition array around random pivot and recursively sort left/right subarrays.
    
    Time Complexity: O(n log n) average, O(n^2) worst case
    Space Complexity: O(log n) average due to recursion
    """
    
    # STEP 1: Handle edge cases
    if len(nums) < 2:
        return nums
    
    # STEP 2: Sort in-place
    _quicksort(nums, 0, len(nums) - 1)
    
    # STEP 3: Return sorted array
    return nums
