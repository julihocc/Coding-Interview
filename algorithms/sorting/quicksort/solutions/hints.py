"""
HINTS: Quicksort

Algorithm: Divide-and-conquer with partitioning
Key insight: Partition array around pivot, recursively sort left and right

Approach: Pick pivot, partition into smaller/larger halves, recurse
"""

from typing import List


def quicksort(H: List[int]) -> List[int]:
    """Sort array in ascending order using quicksort."""
    # STEP 1: Base case - if len(H) <= 1, return H (already sorted)
    # STEP 2: Pick a pivot (e.g., middle element or random)
    # STEP 3: Partition array:
    #   - Create three parts: smaller, equal, greater than pivot
    #   - Or use in-place partitioning with two pointers
    # STEP 4: Recursively sort left (smaller) part
    # STEP 5: Recursively sort right (greater) part
    # STEP 6: Return combined result: left + equal + right
    pass
