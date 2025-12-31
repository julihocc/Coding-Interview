# MinHeap - Pseudocode Guide

## Algorithm Overview
Implement a min-heap using a 1-indexed array. Mirror of MaxHeap: minimum at root, parent ≤ children.

## Key Insight
1-indexed array simplifies parent/child math (same as MaxHeap):
- Parent of i: i // 2
- Left child of i: 2*i
- Right child of i: 2*i + 1

**Key differences from MaxHeap**:
- Heap property: parent ≤ children (not parent ≥)
- Bubble-up: swap if parent > child (not parent <)
- Bubble-down: find SMALLER child (not larger)

## Pseudocode

```
class MinHeap:
    def __init__():
        H = [None]  # Index 0 is unused placeholder
    
    def insert(elt):
        # Step 1: Append to end
        H.append(elt)
        
        # Step 2: Bubble up (swim)
        idx = len(H) - 1
        while idx > 1:
            parent_idx = idx // 2
            
            if H[parent_idx] <= H[idx]:
                break  # Heap property satisfied
            
            # Swap with parent (opposite comparison from MaxHeap!)
            swap H[parent_idx] with H[idx]
            idx = parent_idx
    
    def delete_min():
        # Step 1: Handle empty
        if size == 0:
            return
        
        if size == 1:
            H.pop()
            return
        
        # Step 2: Move last to root
        H[1] = H.pop()
        
        # Step 3: Bubble down (sink)
        idx = 1
        while True:
            left_idx = 2 * idx
            right_idx = 2 * idx + 1
            
            left_val = H[left_idx] if left_idx < len(H) else +inf
            right_val = H[right_idx] if right_idx < len(H) else +inf
            
            if H[idx] <= min(left_val, right_val):
                break  # Heap property satisfied
            
            # Swap with SMALLER child (opposite from MaxHeap!)
            smaller_child_idx = left_idx if left_val <= right_val else right_idx
            swap H[idx] with H[smaller_child_idx]
            idx = smaller_child_idx
```

## Detailed Step-by-Step Implementation

### Insert Operation - O(log n)

**Step 1: Append to end**
- H.append(elt)
- New element is at index len(H) - 1

**Step 2: Bubble up from last position**
- idx = len(H) - 1
- While idx > 1 (not root):
  - parent_idx = idx // 2
  - If H[parent_idx] <= H[idx], heap property satisfied, stop (DIFFERENT from MaxHeap!)
  - Else swap with parent
  - Move to parent: idx = parent_idx

**Why**: New element might be smaller than parent, violating min-heap property. Swap upward until in correct position.

### Delete Min Operation - O(log n)

**Step 1: Handle edge cases**
- If heap empty, return
- If only one element, pop and return

**Step 2: Move last element to root**
- H[1] = H.pop()
- Min element (at root) is removed, last element takes its place

**Step 3: Bubble down from root**
- idx = 1
- While true:
  - left_idx = 2 * idx, right_idx = 2 * idx + 1
  - Get child values (use +inf if child doesn't exist)
  - If H[idx] <= min(left_val, right_val), heap property satisfied, stop
  - Find SMALLER child (DIFFERENT from MaxHeap!)
  - smaller_idx = left if left <= right else right
  - Swap with smaller child
  - idx = smaller_idx

**Why**: Root might be larger than children. Swap downward with smaller child until in correct position.

## Example Trace - Insertions [5, 2, 4, -1, 7]

Insert 5:
- H = [None, 5]
- 5 is root, no parent, stop
- Heap: [None, 5]

Insert 2:
- H = [None, 5, 2]
- idx=2, parent_idx=1, H[1]=5 <= H[2]=2? NO, swap
- H = [None, 2, 5]
- idx=1 (root), stop
- Heap: [None, 2, 5]

Insert 4:
- H = [None, 2, 5, 4]
- idx=3, parent_idx=1, H[1]=2 <= H[3]=4? YES, stop
- Heap: [None, 2, 5, 4]

Insert -1:
- H = [None, 2, 5, 4, -1]
- idx=4, parent_idx=2, H[2]=5 <= H[4]=-1? NO, swap
- H = [None, 2, -1, 4, 5]
- idx=2, parent_idx=1, H[1]=2 <= H[2]=-1? NO, swap
- H = [None, -1, 2, 4, 5]
- idx=1 (root), stop
- Heap: [None, -1, 2, 4, 5] ✓

Insert 7:
- H = [None, -1, 2, 4, 5, 7]
- idx=5, parent_idx=2, H[2]=2 <= H[5]=7? YES, stop
- Heap: [None, -1, 2, 4, 5, 7] ✓

Tree structure:
```
        -1
        / \
       2   4
      / \
     5   7
```

## Example Trace - Delete Min from [None, -1, 2, 4, 5, 7]

Move last (7) to root:
- H = [None, 7, 2, 4, 5]

Bubble down idx=1:
- left_idx=2, H[2]=2
- right_idx=3, H[3]=4
- H[1]=7 <= min(2,4)=2? NO
- Smaller child at idx 2 (value 2)
- Swap: H = [None, 2, 7, 4, 5]
- idx=2

Bubble down idx=2:
- left_idx=4, H[4]=5
- right_idx=5, doesn't exist (use +inf)
- H[2]=7 <= min(5, +inf)=5? NO
- Smaller child at idx 4 (value 5)
- Swap: H = [None, 2, 5, 4, 7]
- idx=4

Bubble down idx=4:
- left_idx=8, doesn't exist (+inf)
- right_idx=9, doesn't exist (+inf)
- H[4]=7 <= min(+inf, +inf)? YES, stop
- Heap: [None, 2, 5, 4, 7] ✓

## Complexity Analysis
- **Insert**: O(log n) - bubble up at most height of tree
- **Delete Min**: O(log n) - bubble down at most height of tree
- **Get Min**: O(1) - access H[1]
- **Space**: O(n) for heap storage

## Comparison with MaxHeap

| Operation | MaxHeap | MinHeap |
|-----------|---------|---------|
| Property | parent ≥ children | parent ≤ children |
| Bubble-up | swap if parent < child | swap if parent > child |
| Bubble-down | find LARGER child | find SMALLER child |
| Sentinel for missing child | -infinity | +infinity |
| Root | Maximum value | Minimum value |
