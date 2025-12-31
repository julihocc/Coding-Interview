"""
HINTS: MinHeap

Algorithm: Heap with bubble-up (insert) and bubble-down (delete)
Key insight: Use 1-indexed array for clean parent/child math (opposite of MaxHeap)

Approach: Maintain min-heap property (parent <= children) with swapping
"""

from typing import List


def solve():
    """Implement MinHeap with insert and delete_min operations."""
    
    class MinHeap:
        def __init__(self):
            """Initialize with 1-indexed array."""
            # STEP 1: Create list with None at index 0 (placeholder)
            pass
        
        def insert(self, elt):
            """Insert element and maintain heap property."""
            # STEP 1: Append element to end
            # STEP 2: Bubble up from last position:
            #   - Compare with parent at idx//2
            #   - If parent > child: swap (opposite of MaxHeap!)
            #   - Continue from parent position
            # STEP 3: Stop when parent <= child or at root
            pass
        
        def delete_min(self):
            """Remove and return minimum (root)."""
            # STEP 1: Handle empty heap
            # STEP 2: Move last element to root
            # STEP 3: Bubble down from root:
            #   - Find SMALLER child (if both exist) - opposite of MaxHeap!
            #   - If root <= smaller child: stop
            #   - Else: swap with smaller child
            # STEP 4: Continue from child position
            pass
    
    return MinHeap
