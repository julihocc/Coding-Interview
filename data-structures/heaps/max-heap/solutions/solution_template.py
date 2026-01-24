"""TEMPLATE: MaxHeap Solution

Class Signature:
    class MaxHeap:

Problem:
    Implement a Max Heap data structure with:
    - insert(elt): Add element, O(log n)
    - delete_max(): Remove max element, O(log n)
    - max_element(): Return max without removing, O(1)
    - size(): Return number of elements, O(1)

Reference: See ../README.md for full problem description
"""


class Solution:
    """Implement MaxHeap using array (1-indexed is often convenient).
    
    Helper index formulas (if 1-indexed):
    - Parent of index i: i // 2
    - Left child of index i: 2 * i
    - Right child of index i: 2 * i + 1
    """
    
    def __init__(self):
        """Initialize empty heap.
        
        Expected behavior:
        - Set up internal array structure (1-indexed or 0-indexed)
        - Initialize to empty state
        """
        # TODO: Set up 1-indexed or 0-indexed array
        pass

    def insert(self, elt):
        """Insert element into heap, maintaining max-heap property.
        
        Expected behavior:
        - Add element to heap
        - Restore max-heap property via bubble-up (sift-up) operation
        - Time: O(log n)
        
        Hint: After appending, compare with parent and swap upward until sorted.
        Use _bubble_up() helper method.
        
        Args:
            elt: The element to insert.
        """
        # TODO: Append element and bubble up
        pass

    def delete_max(self):
        """Remove and return the maximum element.
        
        Expected behavior:
        - Return the root (maximum) element
        - Move last element to root
        - Restore max-heap property via bubble-down (sift-down) operation
        - Time: O(log n)
        
        Hint: After moving last to root, compare with children and swap downward.
        Use _bubble_down() helper method. Handle edge cases: empty heap, single element.
        """
        # TODO: Remove max, move last to root, bubble down
        pass

    def max_element(self):
        """Return the maximum element without removing it.
        
        Expected behavior:
        - Return root element (maximum)
        - Do not modify heap
        - Time: O(1)
        
        Returns:
            The maximum element in the heap.
        """
        # TODO: Return root element
        pass

    def size(self):
        """Return the number of elements in the heap.
        
        Expected behavior:
        - Return count of elements currently stored
        - Time: O(1)
        
        Returns:
            Number of elements in heap.
        """
        # TODO: Return heap size
        pass

    def _bubble_up(self, idx):
        """Restore max-heap property by moving element up.
        
        Swap with parent while element is larger than parent.
        
        Args:
            idx: Index of element to bubble up from.
        """
        # TODO: Compare with parent, swap upward until max-heap property holds
        pass

    def _bubble_down(self, idx):
        """Restore max-heap property by moving element down.
        
        Swap with larger child while element is smaller than a child.
        
        Args:
            idx: Index of element to bubble down from.
        """
        # TODO: Compare with children, swap downward until max-heap property holds
        pass
    
    def size(self):
        """Return number of elements in heap."""
        # TODO: Return heap size
        pass
    
    def max_element(self):
        """Return maximum element (root)."""
        assert self.size() > 0, "Heap is empty"
        # TODO: Return root
        pass
    
    def insert(self, elt):
        """
        Insert element and maintain max-heap property.
        
        Strategy: Add to end, then bubble up.
        Time Complexity: O(log n)
        """
        # TODO: Append to end, then bubble up to correct position
        pass
    
    def delete_max(self):
        """
        Remove and return maximum element.
        Maintain heap property after removal.
        
        Strategy: Replace root with last element, then bubble down.
        Time Complexity: O(log n)
        """
        # TODO: Handle empty heap, remove root, then bubble down
        pass
