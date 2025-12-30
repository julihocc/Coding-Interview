# Quicksort

## Problem Statement

Given an unsorted list of integers, return a new list containing the same elements sorted in non-decreasing order.

## Algorithms

- **Naive:** Use a built-in comparison sort to produce a sorted copy. Complexity: $O(n \log n)$ time, $O(n)$ extra space for the copy.
- **Quicksort (optimized):** In-place quicksort with randomized pivot selection and Hoare-style partitioning to reduce worst-case patterns. Average $O(n \log n)$ time and $O(\log n)$ stack space; worst-case $O(n^2)$ time.

## Function Signature

```python
from typing import List

def quicksort(nums: List[int]) -> List[int]:
    ...
```

## Notes

- Input may be mutated by the optimized solution; tests pass a copy of the data to each solution to avoid cross-test interference.
- Output should always be a sorted list; stability is not required.
