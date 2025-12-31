# Quicksort - Pseudocode Guide

## Algorithm Overview
Divide-and-conquer sorting algorithm. Pick a pivot, partition array around it, then recursively sort the left and right partitions.

## Key Insight
Partitioning rearranges elements so all smaller elements are on the left and all larger on the right. This creates two independent sub-problems that can be solved recursively.

## Pseudocode

```
def quicksort(H):
    # Base case
    if len(H) <= 1:
        return H
    
    # Step 1: Choose pivot (can be middle, first, random, etc.)
    pivot = H[len(H) // 2]
    
    # Step 2: Partition into three groups
    left = []    # Elements < pivot
    middle = []  # Elements == pivot
    right = []   # Elements > pivot
    
    for element in H:
        if element < pivot:
            left.append(element)
        elif element == pivot:
            middle.append(element)
        else:
            right.append(element)
    
    # Step 3: Recursively sort left and right
    return quicksort(left) + middle + quicksort(right)
```

## Detailed Step-by-Step Implementation

**Step 1: Base case**
- If len(H) <= 1, array is already sorted, return H

**Step 2: Choose pivot**
- Can pick any element (middle is safe, random avoids worst case)
- pivot = H[len(H) // 2]

**Step 3: Partition array**
- Create three lists: left (< pivot), middle (== pivot), right (> pivot)
- Iterate through H, append each element to appropriate list

**Step 4: Recursive sort**
- Recursively sort left partition
- Recursively sort right partition
- Combine: sorted_left + middle + sorted_right

**Step 5: Return sorted array**

## Example Trace - Array [5, 2, 8, 1, 9]

Initial call: quicksort([5, 2, 8, 1, 9])
- pivot = H[2] = 8
- Partition:
  - left = [5, 2, 1]
  - middle = [8]
  - right = [9]

Recursive call: quicksort([5, 2, 1])
- pivot = H[1] = 2
- Partition:
  - left = [1]
  - middle = [2]
  - right = [5]
  
  Recursive: quicksort([1]) → [1] (base case)
  Recursive: quicksort([5]) → [5] (base case)
  Result: [1] + [2] + [5] = [1, 2, 5]

Recursive call: quicksort([9]) → [9] (base case)

Final result: [1, 2, 5] + [8] + [9] = [1, 2, 5, 8, 9] ✓

## Complexity Analysis
- **Time**: O(n log n) average case, O(n²) worst case (when pivot is always smallest/largest)
- **Space**: O(n) for creating left/middle/right partitions, O(log n) recursion depth average
- **Note**: Randomizing pivot selection makes O(n²) worst case unlikely
