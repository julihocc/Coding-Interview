"""
HINTS: Left Rotation

Algorithm: Reverse-based rotation
Key insight: Three reversals achieve rotation: reverse(first d), reverse(rest), reverse(all)

Approach: Use reversal operations to rotate array in-place
"""

from typing import List


def left_rotation(arr: List[int], d: int) -> List[int]:
    """Rotate array left by d positions."""
    # STEP 1: Normalize d = d % len(arr) (handle d >= len(arr))
    # STEP 2: Reverse first d elements
    # STEP 3: Reverse remaining elements (from d to end)
    # STEP 4: Reverse entire array
    # STEP 5: Return rotated array
    pass
