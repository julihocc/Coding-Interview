# Left Rotation - Pseudocode Guide

## Algorithm Overview
Rotate array left by d positions using the reversal algorithm: reverse first d, reverse rest, reverse all.

## Key Insight
Three reversals achieve rotation in-place. Mathematical property: Reverse(A) + Reverse(B) + Reverse(A+B) = Rotate left by |A|.

## Pseudocode

```
def left_rotation(arr, d):
    n = len(arr)
    d = d % n  # Normalize d (handle d >= n)
    
    if d == 0:
        return arr
    
    # Step 1: Reverse first d elements
    reverse(arr, 0, d - 1)
    
    # Step 2: Reverse remaining elements (from d to end)
    reverse(arr, d, n - 1)
    
    # Step 3: Reverse entire array
    reverse(arr, 0, n - 1)
    
    return arr

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
```

## Detailed Step-by-Step Implementation

**Step 1: Normalize rotation amount**
- d = d % len(arr)
- Handles cases where d >= len(arr)
- Example: [1, 2, 3, 4, 5] rotated by 7 is same as rotated by 2

**Step 2: Reverse first d elements**
- Call reverse(arr, 0, d-1)
- Use two-pointer approach: swap left and right, move pointers inward

**Step 3: Reverse remaining elements**
- Call reverse(arr, d, len(arr)-1)
- Again use two-pointer swapping

**Step 4: Reverse entire array**
- Call reverse(arr, 0, len(arr)-1)

**Step 5: Return rotated array**

## Example Trace - Array [1, 2, 3, 4, 5], d = 2

Initial: [1, 2, 3, 4, 5], d = 2

Step 1 - Reverse first 2:
- Reverse positions 0-1
- [2, 1, 3, 4, 5]

Step 2 - Reverse from position 2 to end:
- Reverse positions 2-4
- [2, 1, 5, 4, 3]

Step 3 - Reverse entire:
- Reverse positions 0-4
- [3, 4, 5, 1, 2] ✓

Expected result: Elements [1, 2] moved to end, rest shifted left.

## Example Trace - Array [7, 9, 1, 4, 3], d = 3

Initial: [7, 9, 1, 4, 3], d = 3

Step 1 - Reverse first 3:
- [1, 9, 7, 4, 3]

Step 2 - Reverse from position 3:
- [1, 9, 7, 3, 4]

Step 3 - Reverse entire:
- [4, 3, 7, 9, 1] ✓

Expected: [7, 9, 1] move to end, [4, 3] shift to front.

## Why This Works

For array [A][B] where A has d elements and B has n-d elements:

1. Reverse A: [A_reversed][B]
2. Reverse B: [A_reversed][B_reversed]
3. Reverse all: [B] + [A] ✓

This is mathematically sound and works in-place without extra space.

## Complexity Analysis
- **Time**: O(n) - three full reversals, each is O(n)
- **Space**: O(1) - in-place modification, only swap operations

## Alternative Approaches

### Approach 1: Create new array
```
def left_rotation_naive(arr, d):
    d = d % len(arr)
    return arr[d:] + arr[:d]
```
Time: O(n), Space: O(n) - creates new list

### Approach 2: Rotation using temporary
```
def left_rotation_temp(arr, d):
    d = d % len(arr)
    temp = arr[:d]  # Save first d elements
    for i in range(d, len(arr)):
        arr[i-d] = arr[i]
    for i in range(len(arr)-d, len(arr)):
        arr[i] = temp[i - (len(arr)-d)]
    return arr
```
Time: O(n), Space: O(d) - uses temporary storage

**Best approach**: Reversal (in-place, O(1) extra space)
