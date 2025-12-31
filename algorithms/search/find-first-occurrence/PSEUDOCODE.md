# Find First Occurrence - Pseudocode Guide

## Algorithm Overview
Find the leftmost (first) occurrence of a target value in a sorted array using binary search with left-biasing. When target is found, continue searching LEFT to ensure we find the first occurrence.

## Key Insight
Standard binary search stops when target is found. To find the FIRST occurrence, we must keep searching left even after finding the target. This is achieved by setting right = mid - 1 when target is found.

## Pseudocode

```
def find_first_occurrence(H, target):
    left = 0
    right = len(H) - 1
    result = -1  # Default: not found
    
    while left <= right:
        mid = (left + right) // 2
        
        if H[mid] == target:
            result = mid  # Found! Save it.
            right = mid - 1  # Continue searching LEFT
        
        elif H[mid] < target:
            left = mid + 1  # Target is to the right
        
        else:  # H[mid] > target
            right = mid - 1  # Target is to the left
    
    return result
```

## Detailed Step-by-Step Implementation

**Step 1: Initialize variables**
- left = 0 (left boundary)
- right = len(H) - 1 (right boundary)
- result = -1 (track leftmost occurrence)

**Step 2: Binary search with left-biasing**
- While left <= right:
  - mid = (left + right) // 2
  - Three-way comparison:
    - If H[mid] == target: save result = mid, set right = mid - 1 (KEY: keep searching left)
    - If H[mid] < target: set left = mid + 1
    - If H[mid] > target: set right = mid - 1

**Step 3: Return result**
- Returns -1 if never found, or the index of first occurrence

## Example Trace - Array [1, 2, 2, 2, 3], target = 2

Initial: left=0, right=4, result=-1

Iteration 1:
- mid = (0+4)//2 = 2
- H[2] = 2 == 2? YES
- result = 2, right = 1

Iteration 2:
- left=0, right=1
- mid = (0+1)//2 = 0
- H[0] = 1 < 2? YES
- left = 1

Iteration 3:
- left=1, right=1
- mid = (1+1)//2 = 1
- H[1] = 2 == 2? YES
- result = 1, right = 0

Iteration 4:
- left=1, right=0
- Loop ends (left > right)

Return: result = 1 ✓ (first occurrence)

## Example Trace - Array [1, 2, 3], target = 5

Initial: left=0, right=2, result=-1

Iteration 1:
- mid = 1
- H[1] = 2 < 5? YES
- left = 2

Iteration 2:
- left=2, right=2
- mid = 2
- H[2] = 3 < 5? YES
- left = 3

Iteration 3:
- left=3, right=2
- Loop ends (left > right)

Return: result = -1 ✓ (not found)

## Complexity Analysis
- **Time**: O(log n) - binary search eliminates half of remaining elements
- **Space**: O(1) - only use left, right, mid, result variables
