"""TEMPLATE: TopKHeap Solution

Class Signature:
    class TopKHeap:

Problem:
    Implement a data structure that efficiently maintains the k smallest elements:
    - __init__(k): Initialize with capacity k
    - insert(elt): Add element, O(log n) amortized
    - delete_top_k(j): Remove j-th smallest, O(log n) amortized
    - size(): Return number of elements, O(1)

Reference: See ../README.md for full problem description
"""

from typing import List


class TopKHeap:
    """Implement top-k tracking using sorted buffer + overflow heap.
    
    Strategy: Maintain two structures:
    - Sorted array A for k smallest elements (in-order)
    - Min-heap H for overflow elements (larger than A[-1])
    - Only A is directly queryable; H stores excess elements for efficient rebalancing
    """
    
    def __init__(self, k: int):
        """Initialize with capacity k.
        
        Expected behavior:
        - Store parameter k
        - Create sorted buffer A for up to k elements
        - Create min-heap H for overflow
        - Initialize to empty state
        
        Args:
            k: Maximum capacity of top-k structure.
        """
        # TODO: Set up self.k, sorted buffer self.A, and heap self.H
        self.k = k
        pass

    def size(self):
        """Return total number of elements (in A and H combined).
        
        Expected behavior:
        - Return count of all elements stored
        - Time: O(1)
        
        Returns:
            Total number of elements.
        """
        # TODO: Return len(A) + len(H)
        pass

    def insert(self, elt: int) -> None:
        """Insert element while maintaining k smallest.
        
        Expected behavior:
        - If A has room: insert into sorted A via _insert_sorted()
        - If A is full and elt < A[-1]: insert into A, move A[-1] to H
        - If elt >= A[-1]: insert into H
        - Time: O(log n) amortized
        
        Hint: Use sorted insertion for A (O(k) worst case but k is fixed).
        Use heappush/heappop for H (O(log n)).
        
        Args:
            elt: The element to insert.
        """
        # TODO: Maintain k smallest elements across A and H
        pass
    
    def delete_top_k(self, j: int) -> None:
        """Delete j-th smallest element (0-indexed in A).
        
        Expected behavior:
        - Remove A[j]
        - If H is non-empty: pop smallest from H, insert into A via _insert_sorted()
        - Time: O(log n) amortized
        
        Hint: After deletion, replenish A from H if needed to maintain k-sized buffer.
        
        Args:
            j: Index in A (0-indexed, 0 is the smallest).
        """
        # TODO: Remove element and replenish from heap if needed
        pass

    def _insert_sorted(self, elt: int, arr: List[int]) -> None:
        """Insert element into sorted array while maintaining order.
        
        Insert elt into arr such that arr remains sorted.
        Uses insertion sort-like approach for small k.
        
        Args:
            elt: The element to insert.
            arr: The sorted array to insert into.
        """
        # TODO: Append element and shift left until sorted
        # Or use binary search to find position, then shift
        pass

