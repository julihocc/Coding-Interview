# TopKHeap

A data structure for efficiently maintaining the k smallest elements.

## Problem

Implement TopKHeap with the following operations:
- `insert(elt)`: Insert an element (O(k))
- `delete_top_k(j)`: Delete the j-th smallest element (O(k + log n))

Uses a sorted array A for the k smallest elements and a min-heap H for the rest.

## Approaches

- **naive.py**: Basic implementation with sorted array and min-heap
- **optimized.py**: Same efficient approach
