# Quickselect

## Problem Statement

Given an unsorted list of integers and an index `k` (0-indexed), return the `k`-th smallest element. Assume `0 <= k < len(nums)`.

## Algorithms

- **Naive:** Sort the entire list with a comparison sort and return the `k`-th element. Complexity: $O(n \log n)$ time and $O(n)$ space for the sorted copy.
- **Quickselect (average-case optimized):** Use the partition step from Quicksort with a randomized pivot to repeatedly narrow the search interval until the pivot lands at index `k`. Average $O(n)$ time, worst-case $O(n^2)$; in-place partitioning uses $O(1)$ extra space (aside from recursion stack).

## Function Signature

```python
from typing import List

def quickselect(nums: List[int], k: int) -> int:
    ...
```

## Notes

- Inputs are assumed valid (non-empty list and `k` within bounds).
- Implementations may mutate the provided list; callers that need to preserve inputs should pass a copy.
