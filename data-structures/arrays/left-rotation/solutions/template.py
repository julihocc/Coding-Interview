"""TEMPLATE: Left Rotation Solution

Function Signature:
    def rotLeft(a: List[int], d: int) -> List[int]:

Problem:
    Perform d left rotations on array a.
    Return the rotated array.

Reference: See ../README.md for full problem description
"""

from typing import List


def reverse(a: List[int], start: int, end: int) -> None:
    """
    Helper: reverse elements in array from start to end (inclusive).
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # TODO: Implement in-place reversal
    pass


def rotLeft(a: List[int], d: int) -> List[int]:
    """
    Rotate array left by d positions.
    
    APPROACH:
    Consider the reversal algorithm or other rotation techniques.
    
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    
    n = len(a)
    
    # STEP 1: Handle edge cases
    if n == 0:
        return a
    
    # Normalize d (handle d >= n)
    d = d % n
    if d == 0:
        return a
    
    # STEP 2: Create working copy (or modify in-place if allowed)
    result = list(a)
    
    # STEP 3: Implement rotation algorithm
    # TODO: Apply your chosen rotation strategy
    pass
    
    # STEP 4: Return rotated array
    return result
