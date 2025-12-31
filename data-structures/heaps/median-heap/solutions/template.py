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


def solve():
    """
    Implement MedianHeap.
    
    Key insight: Consider using two heaps to track lower and upper halves.
    - One heap for lower half (e.g., max-heap)
    - One heap for upper half (e.g., min-heap)
    
    Maintain balance so median is always accessible.
    """
    
    class MedianHeap:
        def __init__(self):
            """Initialize the median finder."""
            # TODO: Set up data structure(s) for tracking halves
            pass
        
        def size(self):
            """Return total number of elements."""
            # TODO: Return total size
            pass
        
        def addNum(self, num: int) -> None:
            """
            Add a number while maintaining balance.
            Ensure median remains efficiently computable.
            
            Time Complexity: O(log n)
            """
            # TODO: Insert into appropriate heap/section and rebalance
            pass
        
        def findMedian(self) -> float:
            """
            Return current median.
            For odd count: middle value.
            For even count: average of two middle values.
            
            Time Complexity: O(1)
            """
            # TODO: Compute and return median from heap roots
            pass
    
    return MedianHeap
