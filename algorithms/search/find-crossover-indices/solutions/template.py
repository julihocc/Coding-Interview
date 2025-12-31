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
    Binary search helper: find index i in [left, right] where crossover occurs.
    
    Key invariants to maintain:
    - x[left] >= y[left] (left is in "left" region)
    - x[right] < y[right] (right is in "right" region)
    
    Time Complexity: O(log n)
    """
    # TODO: Implement binary search logic
    pass


def findCrossoverIndex(x, y):
    """
    Find the crossover index using binary search.
    
    APPROACH:
    [Describe your strategy here]
    
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    
    # STEP 1: Input validation
    assert len(x) == len(y), "Arrays must have equal length"
    n = len(x)
    
    # STEP 2: Handle edge cases
    if n == 0:
        return -1
    
    # STEP 3: Call binary search helper
    # TODO: Call helper with appropriate bounds
    pass
