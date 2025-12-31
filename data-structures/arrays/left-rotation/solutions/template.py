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
    """Helper: reverse elements in array from start to end (inclusive).
    
    Expected behavior:
    - Reverse elements in-place within range [start, end]
    - Swap first and last, moving inward until indices cross
    - Time Complexity: O(end - start)
    - Space Complexity: O(1)
    
    Args:
        a: Array to reverse within.
        start: Starting index (inclusive).
        end: Ending index (inclusive).
    """
    # TODO: In-place reversal using two pointers
    pass


def rotLeft(a: List[int], d: int) -> List[int]:
    """Rotate array left by d positions.
    
    Expected behavior:
    - Rotate array left by d positions (circular shift)
    - For [1, 2, 3, 4, 5] with d=2, return [3, 4, 5, 1, 2]
    - Handle d >= len(a) via modulo
    - Time Complexity: O(n)
    - Space Complexity: O(n) for output (or O(1) if modifying input in-place)
    
    Hint: Use Reversal Algorithm with three reverse operations:
    1. Reverse first d elements
    2. Reverse remaining elements
    3. Reverse entire array
    This transforms [1,2|3,4,5] -> [2,1|5,4,3] -> [3,4,5,1,2]
    
    Args:
        a: The array to rotate.
        d: Number of left rotations.
    
    Returns:
        Array rotated left by d positions.
    """
    # TODO: Use reversal algorithm to rotate efficiently
    # Remember to handle d % len(a) to normalize rotation count
    pass
    
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
