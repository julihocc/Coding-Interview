# Median Heap - Pseudocode Guide

## Algorithm Overview
Maintain two heaps (max-heap for lower half, min-heap for upper half) to efficiently find median in O(1) with insertion in O(log n).

## Key Insight
- Max-heap stores smaller half of numbers → root is largest of small numbers
- Min-heap stores larger half → root is smallest of large numbers
- Median is always at the root(s): if equal size use average, if unequal use larger heap's root

## Pseudocode

```
class MedianHeap:
    def __init__():
        max_heap = []  # Stores smaller half (max at root)
        min_heap = []  # Stores larger half (min at root)
    
    def add(num):
        # Step 1: Always add to max_heap first
        max_heap.push(num)
        
        # Step 2: Balance heaps
        if max_heap.max > min_heap.min:
            # Root of max_heap should not be > root of min_heap
            val = max_heap.pop()
            min_heap.push(val)
        
        # Step 3: Maintain size invariant
        # Either equal size or max_heap has one more
        if len(max_heap) < len(min_heap) - 1:
            val = min_heap.pop()
            max_heap.push(val)
        
        if len(max_heap) > len(min_heap) + 1:
            val = max_heap.pop()
            min_heap.push(val)
    
    def get_median():
        if len(max_heap) == len(min_heap):
            # Equal sizes: median is average of both roots
            return (max_heap.max + min_heap.min) / 2
        else:
            # Unequal: max_heap has one more (due to invariant)
            return max_heap.max
```

## Detailed Step-by-Step Implementation

### Add Operation - O(log n)

**Step 1: Add to max_heap**
- Always start by adding num to max_heap
- This ensures smaller numbers tend to go there

**Step 2: Balance heaps - maintain property**
- If max_heap.max > min_heap.min:
  - Extract max from max_heap
  - Push to min_heap
  - This preserves property: all in max_heap ≤ all in min_heap

**Step 3: Maintain size invariant**
- After balance step, check sizes
- Maintain: |len(max_heap) - len(min_heap)| ≤ 1
- Preferably: len(max_heap) == len(min_heap) or len(max_heap) == len(min_heap) + 1
- If max_heap too small: move one from min_heap
- If max_heap too large: move one to min_heap

### Get Median - O(1)

**Case 1: Equal sizes**
- Both heaps have n elements
- Median = (max_heap.max + min_heap.min) / 2

**Case 2: Max_heap has one more**
- max_heap has n+1, min_heap has n
- Median = max_heap.max

## Example Trace - Sequence [5, 2, 8, 1, 9]

Insert 5:
- max_heap.push(5) → max_heap = [5]
- max_heap is empty? No check needed
- min_heap = []
- max_heap size = 1, min_heap size = 0 (1 ≤ 0+1) ✓
- Median = 5

Insert 2:
- max_heap.push(2) → max_heap = [5, 2] (heap structure)
- 5 (max of max_heap) > -inf (min_heap empty)? Check if min_heap has elements
- Actually, min_heap empty, so skip balance
- max_heap = [5], min_heap = []
- Wait, max_heap.push(2): max_heap has [5, 2], max is 5
- Size: max=2, min=0. Need to balance: move 1 from max to min
- max_heap.pop() → 5, min_heap.push(5)
- max_heap = [2], min_heap = [5]
- Sizes: 1, 1 (equal) ✓
- Median = (2 + 5) / 2 = 3.5

Insert 8:
- max_heap.push(8) → max_heap = [8, 2]
- max_heap.max = 8 > min_heap.min = 5? YES
- max_heap.pop() → 8, min_heap.push(8)
- max_heap = [2], min_heap = [5, 8]
- Sizes: max=1, min=2. Size difference = 1, but min > max by more
- min_heap.pop() → 5, max_heap.push(5)
- max_heap = [5, 2], min_heap = [8]
- Sizes: 2, 1 ✓ (max has one more)
- Median = 5

Insert 1:
- max_heap.push(1) → max_heap = [5, 2, 1]
- max_heap.max = 5 > min_heap.min = 8? NO
- Size: max=3, min=1. max > min+1
- max_heap.pop() → 5, min_heap.push(5)
- max_heap = [2, 1], min_heap = [5, 8]
- Sizes: 2, 2 (equal) ✓
- Median = (2 + 5) / 2 = 3.5

Insert 9:
- max_heap.push(9) → max_heap = [9, 2, 1]
- max_heap.max = 9 > min_heap.min = 5? YES
- max_heap.pop() → 9, min_heap.push(9)
- max_heap = [2, 1], min_heap = [5, 8, 9]
- Sizes: 2, 3. min > max+1
- min_heap.pop() → 5, max_heap.push(5)
- max_heap = [5, 2, 1], min_heap = [8, 9]
- Sizes: 3, 2. max = min+1 ✓
- Median = 5

Final sequence of medians: 5, 3.5, 5, 3.5, 5

Sorted: [1, 2, 5, 8, 9]
- After 5: [5] → median = 5 ✓
- After 2, 5: [2, 5] → median = 3.5 ✓
- After 2, 5, 8: [2, 5, 8] → median = 5 ✓
- After 1, 2, 5, 8: [1, 2, 5, 8] → median = (2+5)/2 = 3.5 ✓
- After 1, 2, 5, 8, 9: [1, 2, 5, 8, 9] → median = 5 ✓

## Complexity Analysis
- **Add**: O(log n) - insert into heap and rebalance (2 pops, 2 pushes)
- **Get Median**: O(1) - access root(s) directly
- **Space**: O(n) for both heaps combined

## Alternative Approach: Single Heap with Lazy Deletion
- Use one min-heap with (value, is_deleted) pairs
- Remove element by marking deleted (lazy)
- Get median by extracting until non-deleted found
- Trade-off: O(1) delete, O(n) worst-case median (when many lazy deletions)

## Key Invariant
```
All numbers in max_heap ≤ All numbers in min_heap
|len(max_heap) - len(min_heap)| ≤ 1
Preferably: len(max_heap) = len(min_heap) or len(max_heap) = len(min_heap) + 1
```
