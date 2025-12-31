"""
TEMPLATE: Median Heap Solution

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
    [FILL IN: Brief one-liner describing your approach]
    
    APPROACH:
    [Describe your strategy - e.g., Two Heaps (max + min), Single Heap Technique]
    
    Key insight:
    - How can you efficiently track the median?
    - What happens when you add a new number?
    
    Time Complexity:
        - addNum: O(log n)
        - findMedian: O(1)
    """
    
    class MedianHeap:
        def __init__(self):
            """Initialize the median finder."""
            # STEP 1: Set up data structure(s)
            # [Consider: max heap for left half, min heap for right half?]
            # [Or alternative approach?]
            pass
        
        def addNum(self, num: int) -> None:
            """
            Add a number to the structure.
            Maintain balanced distribution for efficient median calculation.
            """
            # STEP 2: Add number
            # - Decide which heap/section to add to
            # - Balance heaps/sections if needed
            # - Maintain invariant for median calculation
            pass
        
        def findMedian(self) -> float:
            """
            Return current median.
            For even count: average of two middle values.
            For odd count: middle value.
            """
            # STEP 3: Calculate and return median
            # - Handle odd vs even counts
            # - Use heap roots efficiently
            pass
    
    return MedianHeap
