# Problem Set #2: Basic Datastructures and Heaps

This folder implements exercises from [docs/ProblemSet2_Solutions.md](../../../docs/ProblemSet2_Solutions.md).

## Structure

- `judge.py` - Test runner that validates all solution implementations
- `solutions/` - Implementation modules for heap data structures
- `tests/` - Test case definitions

## Solution Modules

### Problem 1: MinHeap and TopKHeap

**`problem1_minheap.py`** - Min-heap implementation
- `MinHeap` class with O(log n) insert/delete operations

**`problem1_topk.py`** - Top-K smallest elements data structure
- `TopKHeap` class maintaining k smallest elements efficiently
- Uses sorted array + min-heap hybrid approach

### Problem 2: MaxHeap and MedianMaintainingHeap

**`problem2_maxheap.py`** - Max-heap implementation
- `MaxHeap` class with O(log n) insert/delete operations

**`problem2_median.py`** - Dynamic median computation
- `MedianMaintainingHeap` class using dual heaps (max-heap + min-heap)
- O(log n) insert, O(1) median retrieval

## Usage

### Run all tests
```bash
python data-structures/heaps/problem-set-2/judge.py
```

### Import and use the classes
```python
# Import from solutions package
from data_structures.heaps.problem_set_2.solutions import MinHeap, TopKHeap, MaxHeap, MedianMaintainingHeap

# MinHeap example
heap = MinHeap()
heap.insert(5)
heap.insert(2)
print(heap.min_element())  # 2
heap.delete_min()

# TopKHeap example - maintain 3 smallest elements
topk = TopKHeap(k=3)
for val in [5, 2, 8, 1, 9, 3]:
	topk.insert(val)
print(topk.A)  # [1, 2, 3]

# MedianMaintainingHeap example
median_heap = MedianMaintainingHeap()
for val in [1, 5, 2, 4, 18]:
	median_heap.insert(val)
	print(f"Median: {median_heap.get_median()}")
```

## Implementation Notes

- All heaps use 1-indexed arrays (index 0 is unused)
- Time complexities are documented in docstrings
- `TopKHeap` maintains invariant: all elements in array A ≤ min element in heap H
- `MedianMaintainingHeap` balances two heaps to keep sizes equal or differ by 1

## References

See [docs/ProblemSet2_Solutions.md](../../../docs/ProblemSet2_Solutions.md) for:
- Problem descriptions
- Algorithm design discussions
- Complexity analysis
- Solution explanations
