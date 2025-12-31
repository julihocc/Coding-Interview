"""
HINTS: Top-K Heap

Algorithm: Min-heap of size k to track k largest elements
Key insight: Only keep k elements, use min-heap to quickly remove smallest of top-k

Approach: When new element arrives, compare with min of k-heap, update if needed
"""

from typing import List


def solve():
    """Implement TopKHeap to track k largest elements."""
    
    class TopKHeap:
        def __init__(self, k: int):
            """Initialize heap for k largest elements."""
            # STEP 1: Create min-heap
            # STEP 2: Store k value
            pass
        
        def add(self, num):
            """Add number and maintain top-k invariant."""
            # STEP 1: If heap size < k: just add num
            # STEP 2: If heap size == k:
            #   - Compare num with heap min (root)
            #   - If num > min: remove min and add num
            #   - Else: do nothing (num is not in top-k)
            pass
        
        def get_top_k(self):
            """Return k largest elements."""
            # STEP 1: Extract all elements from heap and sort
            # STEP 2: Return in descending order
            pass
    
    return TopKHeap
