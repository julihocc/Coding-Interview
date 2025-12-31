"""
HINTS: Find First Occurrence

Algorithm: Binary search with left-biasing
Key insight: When target is found, continue searching LEFT to find first occurrence

Approach: Modify standard binary search to keep searching left even after finding target
"""

from typing import List


def find_first_occurrence(nums: List[int], target: int) -> int:
    """Find the FIRST (leftmost) occurrence of target in sorted array."""
    # STEP 1: Initialize left, right boundaries and result = -1
    # STEP 2: Binary search loop - while left <= right:
    #   - Calculate mid
    #   - Compare nums[mid] with target
    #   - If found: save result, move right = mid - 1 (search LEFT)
    #   - If nums[mid] < target: move left = mid + 1
    #   - If nums[mid] > target: move right = mid - 1
    # STEP 3: Return result (-1 if never found)
    pass
