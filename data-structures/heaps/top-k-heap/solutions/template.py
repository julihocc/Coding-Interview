"""
TEMPLATE: Top K Heap Solution

Function Signature:
    def solve():
        # Returns TopKHeap class

Problem:
    Implement a Top K Heap data structure that maintains:
    - add(element): Add element to structure, O(log k)
    - top_k(): Return k largest elements, O(k)
    
    Efficiently track k largest elements seen so far.

Reference: See ../README.md for full problem description
"""


def solve():
    """
    [FILL IN: Brief one-liner describing your approach]
    
    APPROACH:
    [Describe your strategy - e.g., Min Heap of size k, Max Heap technique]
    
    Key insight:
    - Why use a min heap of size k instead of tracking all elements?
    - How do you maintain exactly k largest elements?
    
    Time Complexity:
        - add: O(log k)
        - top_k: O(k)
    Space Complexity: O(k)
    """
    
    class TopKHeap:
        def __init__(self, k: int):
            """
            Initialize heap to track top k elements.
            
            Args:
                k: Number of largest elements to track
            """
            # STEP 1: Set up data structure
            # [Use min heap of size k to track k largest?]
            # [Or alternative approach?]
            self.k = k
            pass
        
        def add(self, element: int) -> None:
            """
            Add element to structure.
            Maintain heap with only k largest elements.
            """
            # STEP 2: Add element
            # - If less than k elements, just add
            # - If element > min in heap, remove min and add element
            # - If element <= min, ignore
            pass
        
        def top_k(self) -> List[int]:
            """
            Return k largest elements (not necessarily sorted).
            """
            # STEP 3: Return top k
            # [Extract from heap and return as list]
            pass
    
    return TopKHeap
