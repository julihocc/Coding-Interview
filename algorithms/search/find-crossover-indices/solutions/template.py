"""TEMPLATE: Find Crossover Indices Solution

Function Signature:
    def findCrossoverIndex(x, y):

Problem:
    Find index i where x[i] >= y[i] and x[i+1] < y[i+1]
    (both x and y are sorted arrays)

Reference: See ../README.md for full problem description
"""


def findCrossoverIndexHelper(x, y, left, right):
    """
    Binary search helper: find index i in [left, right] where x[i] >= y[i] and x[i+1] < y[i+1].
    Maintains invariants: x[left] >= y[left] and x[right] < y[right].
    """
    assert len(x) == len(y)
    assert left >= 0
    assert left <= right - 1
    assert right < len(x)
    
    # Base case: adjacent indices
    if left + 1 == right:
        return left
    
    mid = (left + right) // 2
    
    if x[mid] >= y[mid]:
        # Mid is in the "left" region, continue searching right
        return findCrossoverIndexHelper(x, y, mid, right)
    else:
        # x[mid] < y[mid], mid is in the "right" region, search left
        return findCrossoverIndexHelper(x, y, left, mid)


def findCrossoverIndex(x, y):
    """
    Find the crossover index using binary search.
    
    APPROACH:
    Binary search to find the largest index i where x[i] >= y[i].
    Uses helper function to maintain search invariants.
    
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion
    """
    
    # STEP 1: Input validation
    assert len(x) == len(y), "Arrays must have equal length"
    n = len(x)
    
    # STEP 2: Handle edge cases
    if n == 0:
        return -1
    
    # STEP 3: Call binary search helper
    return findCrossoverIndexHelper(x, y, 0, n - 1)
