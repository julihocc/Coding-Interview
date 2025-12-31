"""
HINTS: Median Heap

Algorithm: Two heaps (max and min) to maintain median
Key insight: Max heap for lower half, min heap for upper half

Approach: Balance sizes so median is always at one of the roots
"""

from typing import List


def solve():
    """Implement MedianHeap with add and get_median operations."""
    
    class MedianHeap:
        def __init__(self):
            """Initialize with two heaps."""
            # STEP 1: Create max_heap for lower half
            # STEP 2: Create min_heap for upper half
            # STEP 3: Keep track of sizes
            pass
        
        def add(self, num):
            """Add number and maintain heap invariants."""
            # STEP 1: Add to max_heap first (lower half)
            # STEP 2: Balance heaps:
            #   - If max_heap max < min_heap min: swap (move roots)
            #   - If size difference > 1: rebalance
            # STEP 3: Maintain invariant: len(max) == len(min) or len(max) == len(min) + 1
            pass
        
        def get_median(self):
            """Return current median."""
            # STEP 1: If heaps equal size: median is average of both roots
            # STEP 2: If max_heap larger: median is max_heap root
            pass
    
    return MedianHeap
