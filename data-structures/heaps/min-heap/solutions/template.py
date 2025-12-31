"""TEMPLATE: MinHeap Solution

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
    Implement MinHeap using 1-indexed array and iterative bubble operations.
    
    APPROACH:
    Use 1-indexed array for convenient parent/child index calculation.
    - Parent of index i: i // 2
    - Left child of index i: 2 * i
    - Right child of index i: 2 * i + 1
    
    Time Complexity:
        - insert: O(log n)
        - delete_min: O(log n)
        - min_element: O(1)
        - size: O(1)
    """
    
    class MinHeap:
        def __init__(self):
            """Initialize empty heap with 1-indexed array."""
            self.H = [None]  # Index 0 unused; heap starts at index 1
        
        def size(self):
            """Return number of elements in heap."""
            return len(self.H) - 1
        
        def min_element(self):
            """Return minimum element (root at index 1)."""
            assert self.size() > 0, "Heap is empty"
            return self.H[1]
        
        def insert(self, elt):
            """
            Insert element into heap and maintain min-heap property.
            Bubble up from end position.
            
            Time Complexity: O(log n)
            """
            self.H.append(elt)
            idx = len(self.H) - 1
            
            # Bubble up: swap with parent while parent > element
            while idx > 1:
                parent_idx = idx // 2
                if self.H[parent_idx] <= self.H[idx]:
                    break
                self.H[parent_idx], self.H[idx] = self.H[idx], self.H[parent_idx]
                idx = parent_idx
        
        def delete_min(self):
            """
            Remove and return minimum element (root).
            Replace with last element and bubble down.
            
            Time Complexity: O(log n)
            """
            if self.size() == 0:
                return
            if self.size() == 1:
                self.H.pop()
                return
            
            # Replace root with last element
            self.H[1] = self.H.pop()
            idx = 1
            
            # Bubble down: swap with smaller child while needed
            while True:
                left = 2 * idx
                right = 2 * idx + 1
                left_val = self.H[left] if left < len(self.H) else float('inf')
                right_val = self.H[right] if right < len(self.H) else float('inf')
                
                if self.H[idx] <= min(left_val, right_val):
                    break
                
                # Swap with smaller child
                child = left if left_val <= right_val else right
                self.H[idx], self.H[child] = self.H[child], self.H[idx]
                idx = child
    
    return MinHeap
