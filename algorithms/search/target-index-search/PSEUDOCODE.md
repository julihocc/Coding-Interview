# Target Index Search - Pseudocode Guide

## Algorithm Overview
Classic binary search to find the index of a target value in a sorted array. Return -1 if target is not found.

## Key Insight
Array is sorted, allowing logarithmic search by eliminating half the search space at each step based on comparison at the midpoint.

## Pseudocode

```
def target_index_search(H, target):
    left = 0
    right = len(H) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if H[mid] == target:
            return mid  # Found!
        
        elif H[mid] < target:
            left = mid + 1  # Target is to the right
        
        else:  # H[mid] > target
            right = mid - 1  # Target is to the left
    
    return -1  # Not found
```

## Detailed Step-by-Step Implementation

**Step 1: Initialize boundaries**
- left = 0 (start of array)
- right = len(H) - 1 (end of array)

**Step 2: Binary search loop**
- While left <= right:
  - mid = (left + right) // 2
  - Three-way comparison:
    - If H[mid] == target: return mid (found!)
    - If H[mid] < target: left = mid + 1 (search right half)
    - If H[mid] > target: right = mid - 1 (search left half)

**Step 3: Return after loop**
- If loop ends without finding target, return -1

## Example Trace - Array [1, 3, 5, 7, 9], target = 5

Initial: left=0, right=4

Iteration 1:
- mid = (0+4)//2 = 2
- H[2] = 5 == 5? YES
- return 2 ✓

## Example Trace - Array [1, 3, 5, 7, 9], target = 6

Initial: left=0, right=4

Iteration 1:
- mid = 2
- H[2] = 5 < 6? YES
- left = 3

Iteration 2:
- left=3, right=4
- mid = (3+4)//2 = 3
- H[3] = 7 > 6? YES
- right = 2

Iteration 3:
- left=3, right=2
- Loop ends (left > right)

Return: -1 ✓ (not found)

## Example Trace - Array [1, 3, 5, 7, 9], target = 1

Initial: left=0, right=4

Iteration 1:
- mid = 2
- H[2] = 5 > 1? YES
- right = 1

Iteration 2:
- left=0, right=1
- mid = (0+1)//2 = 0
- H[0] = 1 == 1? YES
- return 0 ✓

## Complexity Analysis
- **Time**: O(log n) - binary search cuts search space in half each iteration
- **Space**: O(1) - only variable storage
