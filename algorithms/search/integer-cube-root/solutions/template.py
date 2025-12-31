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
    """
    cube = lambda x: x * x * x  # Anonymous function to compute cube
    assert n >= 1
    assert left < right
    assert left >= 0
    assert right < n
    
    mid = (left + right) // 2
    if cube(mid) <= n and cube(mid + 1) > n:
        return mid
    elif cube(mid) > n:
        return integerCubeRootHelper(n, left, mid)
    else:
        return integerCubeRootHelper(n, mid, right)


def integerCubeRoot(n: int) -> int:
    """
    Find integer cube root using binary search.
    
    APPROACH:
    Binary search to find largest k where k^3 <= n.
    Uses helper function to maintain search invariants.
    
    Time Complexity: O(log^2 n) due to repeated cube computations
    Space Complexity: O(log n) due to recursion
    """
    
    # STEP 1: Input validation
    assert n > 0, "Input must be positive"
    
    # STEP 2: Handle edge cases
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    # STEP 3: Call binary search helper
    return integerCubeRootHelper(n, 0, n - 1)
