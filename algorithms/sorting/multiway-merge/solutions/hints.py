"""
HINTS: Multiway Merge

Algorithm: Merge k sorted lists into one sorted list
Key insight: Use pairwise merging or heap to efficiently combine lists

Approach: Either merge pairs recursively, or use a min-heap with pointers
"""

from typing import List


def multiway_merge(lists: List[List[int]]) -> List[int]:
    """Merge k sorted lists into one sorted list."""
    # STEP 1: Base case - if no lists, return empty
    # STEP 2: Option A (Pairwise): Recursively merge lists in pairs
    #   - While more than 1 list: merge pairs
    #   - Repeat until 1 list remains
    # STEP 2: Option B (Heap): Use min-heap with (value, list_idx, element_idx)
    #   - Add first element from each list to heap
    #   - While heap not empty:
    #     * Pop min element, add to result
    #     * Push next element from same list
    # STEP 3: Return merged list
    pass
