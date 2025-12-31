"""
HINTS: Quickselect

Algorithm: Modified quicksort to find k-th smallest element
Key insight: Partition reduces search space to one side only (no need to sort both)

Approach: Partition, compare k with pivot position, recurse on one side
"""

from typing import List


def quickselect(H: List[int], k: int) -> int:
    """Find k-th smallest element (0-indexed) without full sort."""
    # STEP 1: Base case - if list has 1 element, return it
    # STEP 2: Pick a pivot and partition array around it
    # STEP 3: After partition, pivot is at index pivot_idx
    # STEP 4: Compare k with pivot_idx:
    #   - If k == pivot_idx: return pivot value (found!)
    #   - If k < pivot_idx: recurse on LEFT part
    #   - If k > pivot_idx: recurse on RIGHT part (adjust k)
    # STEP 5: Return result from recursion
    pass
