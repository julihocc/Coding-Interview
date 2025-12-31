"""
HINTS: Target Index Search

Algorithm: Classic binary search
Key insight: Array is sorted - allows logarithmic search

Approach: Divide search space in half based on comparison at midpoint
"""

from typing import List


def target_index_search(H: List[int], target: int) -> int:
    """Find index of target in sorted array, return -1 if not found."""
    # STEP 1: Initialize left = 0, right = len(H) - 1
    # STEP 2: Binary search loop - while left <= right:
    #   - Calculate mid
    #   - If H[mid] == target: return mid
    #   - If H[mid] < target: move left = mid + 1
    #   - If H[mid] > target: move right = mid - 1
    # STEP 3: Return -1 (target not found)
    pass
