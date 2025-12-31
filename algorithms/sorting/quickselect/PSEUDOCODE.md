# Quickselect - Pseudocode Guide

## Algorithm Overview
Find the k-th smallest element without fully sorting the array. Like quicksort, but only recurse on one partition based on where k falls.

## Key Insight
After partitioning, the pivot position tells us where the k-th element is. We only need to search one side (either left or right), not both. This gives O(n) average time instead of O(n log n).

## Pseudocode

```
def quickselect(H, k):
    # Base case
    if len(H) == 1:
        return H[0]
    
    # Step 1: Choose pivot and partition
    pivot = H[len(H) // 2]
    
    # Partition into left (< pivot), equal, right (> pivot)
    left = [x for x in H if x < pivot]
    equal = [x for x in H if x == pivot]
    right = [x for x in H if x > pivot]
    
    # Step 2: Determine which partition contains k-th element
    if k < len(left):
        # k-th element is in left partition
        return quickselect(left, k)
    
    elif k < len(left) + len(equal):
        # k-th element is the pivot value
        return equal[0]  # or pivot
    
    else:
        # k-th element is in right partition
        # Note: adjust k for the right partition
        return quickselect(right, k - len(left) - len(equal))
```

## Detailed Step-by-Step Implementation

**Step 1: Base case**
- If len(H) == 1, return H[0] (the only element)

**Step 2: Choose pivot and partition**
- pivot = H[len(H) // 2] (or any element)
- Create three lists:
  - left: all elements < pivot
  - equal: all elements == pivot
  - right: all elements > pivot

**Step 3: Determine which partition contains k-th element**
- If k < len(left): k-th element is in left, recurse on left
- If k < len(left) + len(equal): k-th element is pivot value
- Otherwise: k-th element is in right, recurse on right (adjust k)

**Step 4: Adjust k for right partition**
- New k for right partition = k - len(left) - len(equal)
- This accounts for elements already "skipped"

## Example Trace - Array [5, 2, 8, 1, 9], k = 2 (find 3rd smallest, 0-indexed)

Initial: quickselect([5, 2, 8, 1, 9], 2)
- pivot = H[2] = 8
- left = [5, 2, 1]
- equal = [8]
- right = [9]
- len(left) = 3
- Is k=2 < 3? YES → recurse on left

Call: quickselect([5, 2, 1], 2)
- pivot = H[1] = 2
- left = [1]
- equal = [2]
- right = [5]
- len(left) = 1
- Is k=2 < 1? NO
- Is k=2 < 1+1=2? NO
- Else: recurse on right with k = 2 - 1 - 1 = 0

Call: quickselect([5], 0)
- len(H) == 1 → return 5 ✓

Sorted array would be [1, 2, 5, 8, 9], and 3rd smallest (index 2) is 5. ✓

## Example Trace - Array [3, 1, 4, 1, 5], k = 1 (find 2nd smallest)

Initial: quickselect([3, 1, 4, 1, 5], 1)
- pivot = H[2] = 4
- left = [3, 1, 1] (all < 4)
- equal = [4]
- right = [5]
- len(left) = 3
- Is k=1 < 3? YES → recurse on left

Call: quickselect([3, 1, 1], 1)
- pivot = H[1] = 1
- left = []
- equal = [1, 1]
- right = [3]
- len(left) = 0
- Is k=1 < 0? NO
- Is k=1 < 0+2=2? YES → return equal[0] = 1 ✓

Sorted unique: [1, 3, 4, 5], 2nd smallest is 1. ✓

## Complexity Analysis
- **Time**: O(n) average case - each partition eliminates one side
  - Sum: n + n/2 + n/4 + ... = O(2n) = O(n)
  - Worst case O(n²) if pivot always at boundary
- **Space**: O(n) for creating partitions, O(log n) recursion depth average
- **Key advantage**: Faster than sorting (O(n log n)) when only k-th element needed
