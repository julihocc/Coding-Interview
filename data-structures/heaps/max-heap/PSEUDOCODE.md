# MaxHeap - Pseudocode Guide

## Algorithm Overview
Implement a max-heap using a 1-indexed array. Key operations: insert (bubble-up), delete_max (bubble-down).

## Key Insight
1-indexed array simplifies parent/child math:
- Parent of i: i // 2
- Left child of i: 2*i
- Right child of i: 2*i + 1

## Pseudocode

```
class MaxHeap:
    def __init__():
        H = [None]  # Index 0 is unused placeholder
    
    def insert(elt):
        # Step 1: Append to end
        H.append(elt)
        
        # Step 2: Bubble up (swim)
        idx = len(H) - 1
        while idx > 1:
            parent_idx = idx // 2
            
            if H[parent_idx] >= H[idx]:
                break  # Heap property satisfied
            
            # Swap with parent
            swap H[parent_idx] with H[idx]
            idx = parent_idx
    
    def delete_max():
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
            
            left_val = H[left_idx] if left_idx < len(H) else -inf
            right_val = H[right_idx] if right_idx < len(H) else -inf
            
            if H[idx] >= max(left_val, right_val):
                break  # Heap property satisfied
            
            # Swap with larger child
            larger_child_idx = left_idx if left_val >= right_val else right_idx
            swap H[idx] with H[larger_child_idx]
            idx = larger_child_idx
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
  - If H[parent_idx] >= H[idx], heap property satisfied, stop
  - Else swap with parent: H[parent_idx], H[idx] = H[idx], H[parent_idx]
  - Move to parent: idx = parent_idx

**Why**: New element might violate heap property with parent. Swap upward until in correct position.

### Delete Max Operation - O(log n)

**Step 1: Handle edge cases**
- If heap empty, return
- If only one element, pop and return

**Step 2: Move last element to root**
- H[1] = H.pop()
- Max element (at root) is removed, last element takes its place

**Step 3: Bubble down from root**
- idx = 1
- While true:
  - left_idx = 2 * idx, right_idx = 2 * idx + 1
  - Get child values (use -inf if child doesn't exist)
  - If H[idx] >= max(left_val, right_val), heap property satisfied, stop
  - Find larger child: larger_idx = left if left >= right else right
  - Swap with larger child
  - idx = larger_idx

**Why**: Root might be smaller than children. Swap downward with larger child until in correct position.

## Example Trace - Insertions [5, 2, 4, -1, 7]

Insert 5:
- H = [None, 5]
- 5 is root, no parent, stop
- Heap: [None, 5]

Insert 2:
- H = [None, 5, 2]
- idx=2, parent_idx=1, H[1]=5 >= H[2]=2? YES, stop
- Heap: [None, 5, 2]

Insert 4:
- H = [None, 5, 2, 4]
- idx=3, parent_idx=1, H[1]=5 >= H[3]=4? YES, stop
- Heap: [None, 5, 2, 4]

Insert -1:
- H = [None, 5, 2, 4, -1]
- idx=4, parent_idx=2, H[2]=2 >= H[4]=-1? YES, stop
- Heap: [None, 5, 2, 4, -1]

Insert 7:
- H = [None, 5, 2, 4, -1, 7]
- idx=5, parent_idx=2, H[2]=2 >= H[5]=7? NO, swap
- H = [None, 5, 7, 4, -1, 2]
- idx=2, parent_idx=1, H[1]=5 >= H[2]=7? NO, swap
- H = [None, 7, 5, 4, -1, 2]
- idx=1 (root), stop
- Heap: [None, 7, 5, 4, -1, 2] ✓

Tree structure:
```
       7
      / \
     5   4
    / \
   -1  2
```

## Example Trace - Delete Max from [None, 7, 5, 4, -1, 2]

Move last (2) to root:
- H = [None, 2, 5, 4, -1]

Bubble down idx=1:
- left_idx=2, H[2]=5
- right_idx=3, H[3]=4
- H[1]=2 >= max(5,4)=5? NO
- Larger child at idx 2 (value 5)
- Swap: H = [None, 5, 2, 4, -1]
- idx=2

Bubble down idx=2:
- left_idx=4, H[4]=-1
- right_idx=5, doesn't exist (use -inf)
- H[2]=2 >= max(-1, -inf)=-1? YES, stop
- Heap: [None, 5, 2, 4, -1] ✓

## Complexity Analysis
- **Insert**: O(log n) - bubble up at most height of tree
- **Delete Max**: O(log n) - bubble down at most height of tree
- **Get Max**: O(1) - access H[1]
- **Space**: O(n) for heap storage
