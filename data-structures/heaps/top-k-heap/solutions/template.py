"""TEMPLATE: Top K Heap Solution

Class Signature:
    class TopKHeap:

Problem:
    Implement a Top K Heap data structure that maintains:
    - add(element): Add element to structure, O(log k)
    - top_k(): Return k largest elements, O(k)
    
    Efficiently track k largest elements seen so far.

Reference: See ../README.md for full problem description
"""

from typing import List


class TopKHeap:
    """
    Implement TopKHeap.
    
    Key insight: Maintain only k largest elements efficiently.
    Consider using a min-heap of size k, or hybrid approaches.
    """
    
    def __init__(self, k: int):
        """
        Initialize heap to track top k elements.
        
        Args:
            k: Number of largest elements to track
        """
        self.k = k
        # TODO: Set up data structure(s)
        pass
    
    def size(self):
        """Return total number of elements seen."""
        # TODO: Return total size
        pass
    
    def insert(self, elt: int) -> None:
        """
        Add element while maintaining top k largest.
        
        Strategy: If heap has k elements, only add if larger than min.
        Time Complexity: O(log k)
        """
        # TODO: Insert with size and value constraints
        pass
    
    def top_k(self) -> List[int]:
        """
        Return k largest elements.
        
        Time Complexity: O(k)
        """
        # TODO: Extract and return top k elements
        pass
