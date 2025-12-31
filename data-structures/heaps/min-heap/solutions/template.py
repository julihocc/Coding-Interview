"""
TEMPLATE: MinHeap Solution

Function Signature:
    def solve():
        # Returns MinHeap class

Problem:
    Implement a Min Heap data structure with:
    - insert(elt): Add element, O(log n)
    - delete_min(): Remove min element, O(log n)
    - min_element(): Return min without removing, O(1)
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
        - delete_min: O(log n)
        - min_element: O(1)
    """
    
    class MinHeap:
        def __init__(self):
            """Initialize empty heap."""
            # STEP 1: Set up data structure
            # [Use 1-indexed array or 0-indexed? Choose and document]
            pass
        
        def size(self):
            """Return number of elements in heap."""
            # STEP 2a: Implement size tracking
            pass
        
        def min_element(self):
            """Return minimum element (root)."""
            # STEP 2b: Return root element
            assert self.size() > 0, "Heap is empty"
            pass
        
        def insert(self, elt):
            """
            Insert element into heap.
            Maintain min-heap property: parent <= children
            """
            # STEP 3: Insert element
            # - Add to end
            # - Bubble up: compare with parent, swap if parent > element
            pass
        
        def delete_min(self):
            """
            Remove and return minimum element.
            Maintain heap property after removal.
            """
            # STEP 4: Delete min
            # - Handle empty heap
            # - Replace root with last element
            # - Bubble down: compare with children, swap if needed
            pass
    
    return MinHeap
