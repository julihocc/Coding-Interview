"""
HINTS: Find Crossover Indices

Algorithm: Binary search variant to find crossover point
Key insight: In LEFT region, H[i] >= H[i+1]; in RIGHT region, H[i] < H[i+1]

Approach: Use binary search to find boundary between these regions
"""

from typing import List


def find_crossover_indices(H: List[int]) -> int:
    """
    Find the index where transition from LEFT to RIGHT region occurs.
    LEFT: H[i] >= H[i+1]
    RIGHT: H[i] < H[i+1]
    """
    # STEP 1: Initialize left and right boundaries
    # STEP 2: Binary search loop - while left < right:
    #   - Calculate mid
    #   - Check if mid is in LEFT region: H[mid] >= H[mid+1]?
    #   - If yes, move left boundary (answer is to the right)
    #   - If no, move right boundary (answer is here or to the left)
    # STEP 3: Return left (the crossover index)
    pass
