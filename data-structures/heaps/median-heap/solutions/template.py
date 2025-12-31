"""TEMPLATE: Median Heap Solution

Function Signature:
    def solve():
        # Returns MedianHeap class

Problem:
    Implement a Median Heap data structure that efficiently:
    - addNum(num): Add a number, O(log n)
    - findMedian(): Return current median, O(1)
    
    Median is the middle value(s) in sorted sequence.

Reference: See ../README.md for full problem description
"""

import heapq


def solve():
    """
    Implement MedianHeap using two heaps: max-heap (lower) + min-heap (upper).
    
    APPROACH:
    Maintain two heaps to track lower and upper halves of values.
    - Lower half: stored in max-heap (using negatives in Python)
    - Upper half: stored in min-heap
    - Keep heaps balanced for O(1) median access.
    
    Key insight:
    - Elements in lower heap <= elements in upper heap
    - len(lower) >= len(upper) and len(lower) - len(upper) <= 1
    - Median is root of lower heap (odd count) or average of roots (even count)
    
    Time Complexity:
        - addNum: O(log n)
        - findMedian: O(1)
    """
    
    class MedianHeap:
        def __init__(self):
            """Initialize two heaps for tracking median."""
            self.lower = []  # max-heap (stored as negatives) for lower half
            self.upper = []  # min-heap for upper half
        
        def size(self):
            """Return total number of elements."""
            return len(self.lower) + len(self.upper)
        
        def addNum(self, num: int) -> None:
            """
            Add number while maintaining heap invariants.
            Ensures lower half values <= upper half values.
            Keeps heaps balanced for efficient median computation.
            
            Time Complexity: O(log n)
            """
            # Add to appropriate heap
            if not self.lower or num <= -self.lower[0]:
                heapq.heappush(self.lower, -num)
            else:
                heapq.heappush(self.upper, num)
            
            # Rebalance: maintain len(lower) >= len(upper) and difference <= 1
            if len(self.lower) > len(self.upper) + 1:
                # Move from lower to upper
                max_val = -heapq.heappop(self.lower)
                heapq.heappush(self.upper, max_val)
            elif len(self.upper) > len(self.lower):
                # Move from upper to lower
                min_val = heapq.heappop(self.upper)
                heapq.heappush(self.lower, -min_val)
        
        def findMedian(self) -> float:
            """
            Return current median.
            For odd count: median is root of lower heap.
            For even count: median is average of both roots.
            
            Time Complexity: O(1)
            """
            if not self.lower:
                raise AssertionError("Cannot get median from empty heap")
            
            if len(self.lower) > len(self.upper):
                # Odd count: return root of lower heap
                return float(-self.lower[0])
            else:
                # Even count: return average of both roots
                return (-self.lower[0] + self.upper[0]) / 2.0
    
    return MedianHeap
