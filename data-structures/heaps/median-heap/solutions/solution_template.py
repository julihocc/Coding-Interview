"""TEMPLATE: MedianMaintainingHeap Solution

Class Signature:
    class MedianMaintainingHeap:

Problem:
    Implement a data structure that efficiently tracks the median as elements are inserted:
    - insert(elt): Add element, O(log n)
    - get_median(): Return current median, O(1)
    - size(): Return number of elements, O(1)

Reference: See ../README.md for full problem description
"""



class Solution:
    """Implement median tracking using dual heaps.
    
    Strategy: Maintain two heaps:
    - Max-heap (via negatives in Python's min-heap) for elements below median
    - Min-heap for elements above median
    - Balance sizes to ensure efficient median retrieval
    """
    
    def __init__(self):
        """Initialize two heaps for dual-heap strategy.
        
        Expected behavior:
        - Create max-heap for lower half (using negatives)
        - Create min-heap for upper half
        - Initialize empty state
        """
        # TODO: Set up self.lower (max-heap via negatives) and self.upper (min-heap)
        pass

    def insert(self, elt):
        """Insert element while maintaining median property.
        
        Expected behavior:
        - Add element to appropriate heap (lower or upper)
        - Rebalance heaps to ensure: len(lower) >= len(upper) and |len(lower) - len(upper)| <= 1
        - Median should be median of combined elements
        - Time: O(log n)
        
        Hint: Insert into appropriate heap, then rebalance by moving elements between heaps.
        Use _rebalance() helper method.
        
        Args:
            elt: The element to insert.
        """
        # TODO: Insert into appropriate heap and rebalance
        pass

    def get_median(self):
        """Return the median of all inserted elements.
        
        Expected behavior:
        - If odd count: return middle element
        - If even count: return average of two middle elements
        - Time: O(1)
        
        Returns:
            The median (int or float depending on element count).
        """
        # TODO: Calculate median from heap roots
        pass

    def size(self):
        """Return the total number of elements inserted.
        
        Expected behavior:
        - Return sum of sizes of both heaps
        - Time: O(1)
        
        Returns:
            Total number of elements in both heaps.
        """
        # TODO: Return total element count
        pass

    def _rebalance(self):
        """Rebalance the two heaps to maintain median property.
        
        Ensures: len(lower) >= len(upper) and len(lower) - len(upper) <= 1
        Move elements between heaps to maintain balance.
        """
        # TODO: Balance heaps by moving elements between them
        # Check if lower has too many (> upper + 1), move largest from lower to upper
        # Check if upper has too many (> lower), move smallest from upper to lower
        pass

