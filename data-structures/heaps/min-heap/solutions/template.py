"""TEMPLATE: MinHeap Solution

Class Signature:
    class MinHeap:

Problem:
    Implement a Min Heap data structure with:
    - insert(elt): Add element, O(log n)
    - delete_min(): Remove min element, O(log n)
    - min_element(): Return min without removing, O(1)
    - size(): Return number of elements, O(1)

Reference: See ../README.md for full problem description
"""


class MinHeap:
    """
    Implement MinHeap using array (1-indexed is often convenient).
    
    Helper function suggestions:
    - Parent of index i: i // 2 (if 1-indexed)
    - Left child of index i: 2 * i
    - Right child of index i: 2 * i + 1
    """
    
    def __init__(self):
        """Initialize empty heap."""
        # TODO: Set up 1-indexed or 0-indexed array
        pass
    
    def size(self):
        """Return number of elements in heap."""
        # TODO: Return heap size
        pass
    
    def min_element(self):
        """Return minimum element (root)."""
        assert self.size() > 0, "Heap is empty"
        # TODO: Return root
        pass
    
    def insert(self, elt):
        """
        Insert element and maintain min-heap property.
        
        Strategy: Add to end, then bubble up.
        Time Complexity: O(log n)
        """
        # TODO: Append to end, then bubble up to correct position
        pass
    
    def delete_min(self):
        """
        Remove and return minimum element.
        Maintain heap property after removal.
        
        Strategy: Replace root with last element, then bubble down.
        Time Complexity: O(log n)
        """
        # TODO: Handle empty heap, remove root, then bubble down
        pass
