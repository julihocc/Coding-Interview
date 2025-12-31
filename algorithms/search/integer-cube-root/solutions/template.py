"""TEMPLATE: Integer Cube Root Solution

Function Signature:
    def integerCubeRoot(n: int) -> int:

Problem:
    Find the largest integer k such that k^3 <= n.

Reference: See ../README.md for full problem description
"""


def integerCubeRootHelper(n, left, right):
    """
    Binary search helper: find largest k in [left, right] where k^3 <= n.
    
    Tip: Use a lambda to compute cubes efficiently.
    
    Time Complexity: O(log n * log n) due to cube operations
    """
    # TODO: Implement binary search with cube comparisons
    pass


def integerCubeRoot(n: int) -> int:
    """
    Find integer cube root using binary search.
    
    APPROACH:
    [Describe your strategy here]
    
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    
    # STEP 1: Input validation
    assert n > 0, "Input must be positive"
    
    # STEP 2: Handle edge cases
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    # STEP 3: Call binary search helper
    # TODO: Call helper with appropriate bounds
    pass
