"""
TEMPLATE: MaxHeap Solution

Function Signature:
    def solve():
        # Returns MaxHeap class

Problem:
    Implement a Max Heap data structure with:
    - insert(elt): Add element, O(log n)
    - delete_max(): Remove max element, O(log n)
    - max_element(): Return max without removing, O(1)
    - size(): Return number of elements, O(1)

Reference: See ../README.md for full problem description
"""


def solve():
    """
    [FILL IN: Brief one-liner describing your approach]
    
    APPROACH:
    [Describe your strategy - e.g., Recursive Bubbling, Iterative Bubbling]
    
    Key design choices:
    - 1-indexed array for easier parent/child calculation?
    - Recursive or iterative bubble operations?
    
    Time Complexity:
        - insert: O(log n)
        - delete_max: O(log n)
        - max_element: O(1)
    """
    
    class MaxHeap:
        def __init__(self):
            """Initialize empty heap."""
            # STEP 1: Set up data structure
            # [Use 1-indexed array or 0-indexed? Choose and document]
            pass
        
        def size(self):
            """Return number of elements in heap."""
            # STEP 2a: Implement size tracking
            pass
        
        def max_element(self):
            """Return maximum element (root)."""
            # STEP 2b: Return root element
            assert self.size() > 0, "Heap is empty"
            pass
        
        def insert(self, elt):
            """
            Insert element into heap.
            Maintain max-heap property: parent >= children
            """
            # STEP 3: Insert element
            # - Add to end
            # - Bubble up: compare with parent, swap if needed
            pass
        
        def delete_max(self):
            """
            Remove and return maximum element.
            Maintain heap property after removal.
            """
            # STEP 4: Delete max
            # - Handle empty heap
            # - Replace root with last element
            # - Bubble down: compare with children, swap if needed
            pass
    
    return MaxHeap
