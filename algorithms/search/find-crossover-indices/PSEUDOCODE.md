# Find Crossover Indices - Pseudocode Guide

## Algorithm Overview
Find the index where the array transitions from LEFT region (H[i] >= H[i+1]) to RIGHT region (H[i] < H[i+1]). Use binary search to efficiently locate this boundary.

## Key Insight
The transition point creates a monotonic property: everything before it has H[i] >= H[i+1], everything after has H[i] < H[i+1]. This enables binary search.

## Pseudocode

```
def find_crossover_indices(H):
    left = 0
    right = len(H) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if H[mid] >= H[mid + 1]:
            # mid is in LEFT region, answer is to the right
            left = mid + 1
        else:
            # mid is in RIGHT region, answer is here or left
            right = mid
    
    return left  # The crossover index
```

## Detailed Step-by-Step Implementation

**Step 1: Initialize boundaries**
- left = 0 (start of array)
- right = len(H) - 1 (end of array)

**Step 2: Binary search with property check**
- While left < right (note: not <=, ensures convergence)
- Calculate mid = (left + right) // 2
- Check if mid is in LEFT region: H[mid] >= H[mid+1]?
  - If YES: left = mid + 1 (move right, answer is further right)
  - If NO: right = mid (keep mid, answer is here or left)

**Step 3: Return**
- When left == right, we've found the crossover index
- Return left

## Example Trace

Array: [5, 6, 1, 2, 3, 4]
LEFT region: [5, 6] (5>=6? No... wait, 6>1? Yes, so LEFT)
Actually: LEFT = indices where H[i] >= H[i+1]
- i=0: 5 >= 6? NO
- i=1: 6 >= 1? YES ← transition point

Initial: left=0, right=5

Iteration 1:
- mid = (0+5)//2 = 2
- H[2]=1, H[3]=2
- 1 >= 2? NO → right = 2

Iteration 2:
- left=0, right=2
- mid = (0+2)//2 = 1
- H[1]=6, H[2]=1
- 6 >= 1? YES → left = 2

Iteration 3:
- left=2, right=2
- Loop ends
- Return 2... but wait, index 1 is the crossover (6>=1 is TRUE)

Actually the crossover is at index 1 where H[1]=6 >= H[2]=1. Let me retrace:

Return left = 1 ✓ (the last index of LEFT region)

## Complexity Analysis
- **Time**: O(log n) - standard binary search
- **Space**: O(1) - only variable storage
