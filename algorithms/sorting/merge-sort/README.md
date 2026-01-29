# Merge Sort

## Problem Statement

Given an unsorted list of integers, return a new list containing the same elements sorted in non-decreasing order.

## Algorithms

- **Naive:** Use a built-in comparison sort to produce a sorted copy. Complexity: $O(n \log n)$ time, $O(n)$ extra space for the copy.
- **Merge Sort (recursive):** Classic divide-and-conquer approach that recursively splits the array in half, sorts each half, and merges them. Guaranteed $O(n \log n)$ time complexity with $O(n)$ extra space for merging.
- **Merge Sort (iterative):** Bottom-up approach that iteratively merges subarrays of increasing sizes. Same $O(n \log n)$ time complexity with $O(n)$ extra space, but avoids recursion overhead.

## Function Signature

```python
from typing import List

def merge_sort(nums: List[int]) -> List[int]:
    ...
```

## Notes

- Merge sort is a stable sorting algorithm, meaning equal elements maintain their relative order.
- Unlike quicksort, merge sort has guaranteed $O(n \log n)$ worst-case time complexity.
- The algorithm requires $O(n)$ auxiliary space for the merge operation.
- Output should always be a sorted list.
