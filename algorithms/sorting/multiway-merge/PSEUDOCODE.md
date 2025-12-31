# Multiway Merge - Pseudocode Guide

## Algorithm Overview
Merge k sorted lists into one sorted list. Can use either pairwise merging or a heap-based approach for efficiency.

## Key Insight
When merging sorted lists, we can either:
1. **Pairwise**: Merge lists in pairs recursively
2. **Heap**: Maintain a min-heap of (value, list_index, element_index) to always pick the smallest next element

## Pseudocode - Approach A: Pairwise Merging

```
def multiway_merge_pairwise(lists):
    if not lists:
        return []
    
    # Keep merging pairs until one list remains
    while len(lists) > 1:
        merged_lists = []
        
        # Merge pairs
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                # Merge lists[i] and lists[i+1]
                merged = merge_two(lists[i], lists[i+1])
            else:
                # Odd one out, add as-is
                merged = lists[i]
            
            merged_lists.append(merged)
        
        lists = merged_lists
    
    return lists[0] if lists else []

def merge_two(list1, list2):
    result = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    # Append remaining elements
    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result
```

## Pseudocode - Approach B: Heap-Based

```
import heapq

def multiway_merge_heap(lists):
    if not lists:
        return []
    
    # Create min-heap with (value, list_idx, element_idx)
    min_heap = []
    
    # Add first element from each list
    for list_idx, lst in enumerate(lists):
        if lst:  # Skip empty lists
            heapq.heappush(min_heap, (lst[0], list_idx, 0))
    
    result = []
    
    while min_heap:
        value, list_idx, elem_idx = heapq.heappop(min_heap)
        result.append(value)
        
        # If there are more elements in this list, push the next one
        if elem_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_value, list_idx, elem_idx + 1))
    
    return result
```

## Detailed Step-by-Step Implementation

### Approach A: Pairwise

**Step 1: Check for empty input**
- If lists is empty, return []

**Step 2: Repeatedly merge pairs**
- While more than one list remains:
  - For each pair of lists, merge them
  - Add merged result to new list
  - If odd number of lists, add the last one as-is

**Step 3: Merge two sorted lists**
- Use two pointers (i, j) starting at 0
- Compare elements at each position
- Append the smaller one to result
- Move the corresponding pointer forward
- After one list exhausted, append remaining from other list

### Approach B: Heap-Based

**Step 1: Initialize min-heap**
- For each list, push (first_element, list_index, 0) to heap

**Step 2: Extract and merge**
- While heap not empty:
  - Pop minimum (value, list_idx, elem_idx)
  - Add value to result
  - If next element exists in that list, push it to heap

**Step 3: Return merged result**

## Example Trace - Lists [[1, 3, 5], [2, 4], [1, 2, 3]]

### Using Pairwise Merge:

Initial: [[1, 3, 5], [2, 4], [1, 2, 3]]

Round 1:
- Merge [1, 3, 5] and [2, 4] → [1, 2, 3, 4, 5]
- [1, 2, 3] stays as-is
- Result: [[1, 2, 3, 4, 5], [1, 2, 3]]

Round 2:
- Merge [1, 2, 3, 4, 5] and [1, 2, 3] → [1, 1, 2, 2, 3, 3, 4, 5]
- Result: [[1, 1, 2, 2, 3, 3, 4, 5]]

Final: [1, 1, 2, 2, 3, 3, 4, 5] ✓

### Using Heap:

Initial heap: [(1, 0, 0), (2, 1, 0), (1, 2, 0)]
After heapify: [(1, 0, 0), (1, 2, 0), (2, 1, 0)]

Pop (1, 0, 0) → result = [1], push (3, 0, 1)
Pop (1, 2, 0) → result = [1, 1], push (2, 2, 1)
Pop (2, 1, 0) → result = [1, 1, 2], push (4, 1, 1)
Pop (2, 2, 1) → result = [1, 1, 2, 2], push (3, 2, 2)
Pop (3, 0, 1) → result = [1, 1, 2, 2, 3], push (5, 0, 2)
Pop (3, 2, 2) → result = [1, 1, 2, 2, 3, 3]
Pop (4, 1, 1) → result = [1, 1, 2, 2, 3, 3, 4]
Pop (5, 0, 2) → result = [1, 1, 2, 2, 3, 3, 4, 5]

Final: [1, 1, 2, 2, 3, 3, 4, 5] ✓

## Complexity Analysis

### Pairwise Approach:
- **Time**: O(n log k) where n = total elements, k = number of lists
  - Each merge is O(n), and there are O(log k) rounds
- **Space**: O(n) for merged result

### Heap Approach:
- **Time**: O(n log k) where n = total elements, k = number of lists
  - n insertions/extractions from heap, each O(log k)
- **Space**: O(n) for result, O(k) for heap
