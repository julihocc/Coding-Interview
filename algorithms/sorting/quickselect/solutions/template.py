"""TEMPLATE: Quickselect Solution

Function Signature:
    def quickselect(nums: List[int], k: int) -> int:

Problem:
    Find the k-th smallest element (0-indexed) in unsorted array.
    
Reference: See ../README.md for full problem description
"""

import random
from typing import List


def _partition(arr: List[int], left: int, right: int, pivot_index: int) -> int:
    """
    Helper function: partition array around pivot.
    Moves pivot to final sorted position and returns that position.
    
    Time Complexity: O(n)
    """
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    store_index = left
    
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    
    arr[right], arr[store_index] = arr[store_index], arr[right]
    return store_index


def quickselect(nums: List[int], k: int) -> int:
    """
    Find k-th smallest element using quickselect.
    
    APPROACH:
    Use randomized partition to divide array and recursively search relevant half.
    Average time is linear; avoids full sorting.
    
    Time Complexity: O(n) average, O(n^2) worst case
    Space Complexity: O(log n) average due to recursion
    """
    
    # STEP 1: Input validation
    if not nums:
        raise ValueError("nums must be non-empty")
    assert 0 <= k < len(nums), "k must be valid index"
    
    # STEP 2: Initialize search bounds
    left, right = 0, len(nums) - 1
    
    # STEP 3: Quickselect loop
    while True:
        if left == right:
            return nums[left]
        
        # Choose random pivot and partition
        pivot_index = random.randint(left, right)
        pivot_index = _partition(nums, left, right, pivot_index)
        
        # Check if we found k-th smallest
        if pivot_index == k:
            return nums[pivot_index]
        elif pivot_index < k:
            left = pivot_index + 1
        else:
            right = pivot_index - 1
