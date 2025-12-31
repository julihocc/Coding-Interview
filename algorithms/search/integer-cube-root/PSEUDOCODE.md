# Integer Cube Root - Pseudocode Guide

## Algorithm Overview
Find the largest integer x such that x³ ≤ n. Use binary search on the range [0, n] to efficiently locate this boundary.

## Key Insight
The cubic function is strictly monotonic: if x³ > n, then all y > x have y³ > n. This monotonicity allows binary search to find the answer in logarithmic time.

## Pseudocode

```
def integer_cube_root(n):
    left = 0
    right = n
    
    while left <= right:
        mid = (left + right) // 2
        cube = mid * mid * mid
        
        if cube == n:
            return mid  # Exact cube root found
        
        elif cube < n:
            left = mid + 1  # mid is valid, search for larger
        
        else:  # cube > n
            right = mid - 1  # mid is too large, search smaller
    
    return right  # right is largest value where right³ <= n
```

## Detailed Step-by-Step Implementation

**Step 1: Initialize search space**
- left = 0 (smallest possible cube root: 0³ = 0)
- right = n (largest candidate to check)

**Step 2: Binary search loop**
- While left <= right:
  - mid = (left + right) // 2
  - cube = mid × mid × mid
  - Three-way comparison:
    - If cube == n: return mid (exact match)
    - If cube < n: left = mid + 1 (search for larger)
    - If cube > n: right = mid - 1 (search for smaller)

**Step 3: Return after loop**
- When loop ends (left > right), right is the answer
- right is the largest integer where right³ ≤ n

## Example Trace - n = 8

Initial: left=0, right=8

Iteration 1:
- mid = (0+8)//2 = 4
- cube = 4³ = 64
- 64 > 8? YES → right = 3

Iteration 2:
- left=0, right=3
- mid = (0+3)//2 = 1
- cube = 1³ = 1
- 1 < 8? YES → left = 2

Iteration 3:
- left=2, right=3
- mid = (2+3)//2 = 2
- cube = 2³ = 8
- 8 == 8? YES → return 2 ✓

## Example Trace - n = 30

Initial: left=0, right=30

Iteration 1:
- mid = 15, cube = 3375 > 30 → right = 14

Iteration 2:
- mid = 7, cube = 343 > 30 → right = 6

Iteration 3:
- mid = 3, cube = 27 < 30 → left = 4

Iteration 4:
- mid = 5, cube = 125 > 30 → right = 4

Iteration 5:
- mid = 4, cube = 64 > 30 → right = 3

Iteration 6:
- left=4, right=3 → loop ends

Return: right = 3 ✓ (3³ = 27 ≤ 30 < 64 = 4³)

## Complexity Analysis
- **Time**: O(log n) - binary search on range [0, n]
- **Space**: O(1) - only variable storage
