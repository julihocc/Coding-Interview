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
    Helper function: reverse elements in array from start to end (inclusive).
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1


def rotLeft(a: List[int], d: int) -> List[int]:
    """
    Rotate array left by d positions using reversal algorithm.
    
    APPROACH:
    1. Reverse first d elements
    2. Reverse remaining n-d elements
    3. Reverse entire array
    Result: array rotated left by d positions.
    
    Time Complexity: O(n)
    Space Complexity: O(1) auxiliary (though we create a copy of the array)
    """
    
    n = len(a)
    
    # STEP 1: Handle edge cases
    if n == 0:
        return a
    
    # Normalize d (handle d >= n)
    d = d % n
    if d == 0:
        return a
    
    # STEP 2: Create a copy to avoid modifying input
    result = list(a)
    
    # STEP 3: Apply reversal algorithm
    # Reverse first d elements
    reverse(result, 0, d - 1)
    
    # Reverse remaining n - d elements
    reverse(result, d, n - 1)
    
    # Reverse entire array
    reverse(result, 0, n - 1)
    
    # STEP 4: Return rotated array
    return result
