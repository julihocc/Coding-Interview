"""
TEMPLATE: Left Rotation Solution

Function Signature:
    def rotLeft(a: List[int], d: int) -> List[int]:

Problem:
    Perform d left rotations on array a.
    Return the rotated array.

Reference: See ../README.md for full problem description
"""

from typing import List


def rotLeft(a: List[int], d: int) -> List[int]:
    """
    [FILL IN: Brief one-liner describing your approach]
    
    APPROACH:
    [Describe your strategy here - e.g., Iterative Rotation, Reversal Algorithm]
    
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    
    n = len(a)
    
    # STEP 1: Input validation and edge cases
    if n == 0:
        return a
    
    # Normalize d (handle d >= n)
    d = d % n
    if d == 0:
        return a
    
    # STEP 2: Initialize data structures
    # [Set up any variables needed]
    
    # STEP 3: Main algorithm
    # [Implement your rotation logic here]
    pass
    
    # STEP 4: Return rotated array
    # [return result]
