# Descending Quicksort

## Problem Statement

Given an unsorted list of integers, return a new list containing the same elements sorted in descending order (from largest to smallest).

## Algorithms

- **Quicksort (descending):** In-place quicksort with randomized pivot selection. Modified partition logic to sort elements such that larger elements come before smaller ones. Average $O(n \log n)$ time, worst-case $O(n^2)$ time.

## Function Signature

```python
from typing import List

def quicksort_descending(nums: List[int]) -> List[int]:
    ...
```
