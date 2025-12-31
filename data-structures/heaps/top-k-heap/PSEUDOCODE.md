# Top-K Heap - Pseudocode Guide

## Algorithm Overview
Maintain a min-heap of size k to track the k largest elements seen so far. When a new element arrives, compare with heap minimum and update if necessary.

## Key Insight
- Use a **min-heap** (not max-heap) to store k largest elements
- Min of heap is smallest of the k largest → easy to evict if new element is larger
- O(n log k) to process n elements with heap operations
- Only track k elements at a time (space efficient)

## Pseudocode

```
class TopKHeap:
    def __init__(k):
        heap = []  # Min-heap
        self.k = k
    
    def add(num):
        if len(heap) < k:
            # Still building heap, just add
            heap.push(num)
        else:
            # Heap full, check if num should replace min
            if num > heap.min():
                heap.pop()  # Remove minimum
                heap.push(num)  # Add new element
            # else: num is not in top-k, ignore
    
    def get_top_k():
        result = []
        temp_heap = copy(heap)
        
        # Extract all and sort descending
        while temp_heap not empty:
            result.append(temp_heap.pop())  # Pop min
        
        result.reverse()  # Now in descending order
        return result
```

## Detailed Step-by-Step Implementation

### Initialization - O(1)

**Step 1: Create empty min-heap**
- heap = [] (will be min-heap)
- Store k value

### Add Operation - O(log k)

**Step 1: Check if heap not full**
- If len(heap) < k:
  - Just push num to heap
  - Continue building heap

**Step 2: Heap is full**
- If num > heap.min():
  - Remove minimum (root of min-heap)
  - Push num to heap
  - Heap now contains k largest elements seen
- Else:
  - num is not in top-k, ignore (don't add)

**Why this works**:
- Heap always contains k largest elements so far
- New element either enters heap (if larger than current minimum) or is discarded
- Heap minimum is the smallest of the k largest

### Get Top-K Operation - O(k log k)

**Step 1: Copy heap**
- Create temporary copy to avoid modifying original

**Step 2: Extract all elements**
- While heap not empty:
  - Pop minimum element
  - Add to result
  - Elements come out in ascending order (from smallest to largest of top-k)

**Step 3: Reverse to get descending order**
- Reverse result to get k largest in descending order

## Example Trace - Sequence [3, 1, 5, 4, 2, 8, 6], k=3

Add 3:
- heap size=0 < k=3, push 3
- heap = [3]

Add 1:
- heap size=1 < k=3, push 1
- heap = [1, 3] (min-heap: 1 at root)

Add 5:
- heap size=2 < k=3, push 5
- heap = [1, 3, 5]

Add 4:
- heap size=3 == k=3, 4 > heap.min()=1? YES
- Pop 1, push 4
- heap = [3, 4, 5]

Add 2:
- heap size=3, 2 > heap.min()=3? NO
- Ignore 2

Add 8:
- heap size=3, 8 > heap.min()=3? YES
- Pop 3, push 8
- heap = [4, 5, 8]

Add 6:
- heap size=3, 6 > heap.min()=4? YES
- Pop 4, push 6
- heap = [5, 6, 8]

Get top-k:
- Extract from min-heap: 5, 6, 8
- Result = [5, 6, 8]
- Reverse: [8, 6, 5] ✓ (3 largest in descending order)

Verify: sequence sorted = [1, 2, 3, 4, 5, 6, 8], top 3 largest = [8, 6, 5] ✓

## Example Trace - Sequence [10, 3, 8, 2, 15, 7, 1], k=2

Add 10:
- heap = [10]

Add 3:
- heap = [3, 10]

Add 8:
- heap size=2 == k=2, 8 > heap.min()=3? YES
- Pop 3, push 8
- heap = [8, 10]

Add 2:
- heap size=2, 2 > heap.min()=8? NO
- Ignore

Add 15:
- heap size=2, 15 > heap.min()=8? YES
- Pop 8, push 15
- heap = [10, 15]

Add 7:
- heap size=2, 7 > heap.min()=10? NO
- Ignore

Add 1:
- heap size=2, 1 > heap.min()=10? NO
- Ignore

Get top-k:
- Extract: 10, 15
- Result = [10, 15]
- Reverse: [15, 10] ✓

Verify: 2 largest in [10, 3, 8, 2, 15, 7, 1] = [15, 10] ✓

## Complexity Analysis
- **Add**: O(log k) - heap operation on k elements
- **Get Top-K**: O(k log k) - extract k elements from heap
- **Space**: O(k) - only store k elements

## Processing n elements:
- **Time**: O(n log k) - n additions, each O(log k)
- Much faster than sorting (O(n log n)) when k << n

## Alternative Approach: Max-Heap with Removal

```
class TopKHeapMaxHeap:
    def __init__(k):
        heap = []  # Max-heap
        self.k = k
    
    def add(num):
        if len(heap) < k:
            heap.push(num)
        elif num > heap.min():
            # Have to find and remove minimum from max-heap
            # This is O(k) not O(log k)!
            find_and_remove_min(heap)
            heap.push(num)
```

**Problem**: Finding and removing min from max-heap takes O(k) time, making add O(k).
**Solution**: Use min-heap as shown in main pseudocode.

## When to Use Top-K Heap
- **Streaming data**: Process elements one-by-one without storing all
- **Find k largest**: Don't need to sort entire array
- **Limited memory**: Only store k elements
- **Large n, small k**: n=1,000,000 and k=100 → much faster than sorting
