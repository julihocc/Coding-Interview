# MedianHeap

A data structure for efficiently computing the median of a dynamic dataset.

## Problem

Implement MedianMaintainingHeap with the following operations:
- `insert(elt)`: Insert an element (O(log n))
- `get_median()`: Get the median (O(1))

Uses two heaps: a max-heap for the smaller half and a min-heap for the larger half.

## Approaches

- **naive.py**: Basic implementation with proper heap balancing
- **optimized.py**: Same efficient approach
