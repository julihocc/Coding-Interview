"""TEMPLATE: Top K Heap Solution

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

from typing import List
import heapq


def solve():
    """
    Implement TopKHeap using hybrid storage: sorted buffer + overflow heap.
    
    APPROACH:
    Maintain k smallest values in sorted buffer A and overflow in min-heap H.
    - Top k largest = contents of buffer A
    - When new element arrives:
      * If < A[-1] and A is full, replace and push displaced to H
      * Otherwise, push to H
    
    Key insight:
    - Min-heap H contains elements not in top k
    - Sorted buffer A contains current top k
    - Insert maintains both: O(log k) + O(k) sorting, amortized O(log k)
    - Access is O(k) to return A
    
    Time Complexity:
        - insert: O(log k) heap op + O(k) insertion in sorted buffer
        - top_k: O(k) to copy buffer
    Space Complexity: O(k)
    """
    
    class TopKHeap:
        def __init__(self, k: int):
            """
            Initialize structure to track top k largest elements.
            
            Args:
                k: Number of largest elements to track
            """
            self.k = k
            self.A = []  # Sorted buffer of k smallest (from top k)
            self.H = []  # Min-heap for overflow elements
        
        def size(self):
            """Return total number of elements seen."""
            return len(self.A) + len(self.H)
        
        def insert(self, elt: int) -> None:
            """
            Add element while maintaining top k largest.
            
            Time Complexity: O(log k) + O(k) amortized
            """
            if len(self.A) < self.k:
                # Buffer not full, insert into sorted buffer
                idx = len(self.A)
                self.A.append(elt)
                # Maintain sorted order by shifting
                while idx > 0 and self.A[idx] < self.A[idx - 1]:
                    self.A[idx], self.A[idx - 1] = self.A[idx - 1], self.A[idx]
                    idx -= 1
                return
            
            # Buffer is full
            if elt < self.A[-1]:
                # Element is in top k, replace smallest
                self.A.append(elt)
                idx = len(self.A) - 1
                while idx > 0 and self.A[idx] < self.A[idx - 1]:
                    self.A[idx], self.A[idx - 1] = self.A[idx - 1], self.A[idx]
                    idx -= 1
                # Displace last element to overflow heap
                displaced = self.A.pop()
                heapq.heappush(self.H, displaced)
            else:
                # Element not in top k, push to overflow heap
                heapq.heappush(self.H, elt)
        
        def delete_top_k(self, j: int) -> None:
            """
            Helper: remove element at position j from top k buffer,
            refilling from overflow heap if available.
            """
            assert 0 <= j < len(self.A)
            del self.A[j]
            if self.H:
                # Refill from overflow heap
                min_val = heapq.heappop(self.H)
                # Insert back into sorted position
                self.A.append(min_val)
                idx = len(self.A) - 1
                while idx > 0 and self.A[idx] < self.A[idx - 1]:
                    self.A[idx], self.A[idx - 1] = self.A[idx - 1], self.A[idx]
                    idx -= 1
    
    return TopKHeap
