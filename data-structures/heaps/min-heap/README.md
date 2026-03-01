# MinHeap

A min-heap data structure implementation.

## Problem

Implement a MinHeap with the following operations:

- `insert(elt)`: Insert an element (O(log n))
- `delete_min()`: Remove the minimum element (O(log n))
- `min_element()`: Get the minimum element (O(1))
- `size()`: Get the number of elements

## Scenario

Imagine tracking spacecraft license numbers from a faraway galaxy. You need to
efficiently insert incoming license numbers and remove the spacecraft with the
smallest license number once it leaves your radar.

## Approaches

- **solution_naive.py**: O(n) insert and delete via unsorted list
- **solution_optimized.py**: O(log n) insert and delete via custom 1-indexed array (iterative bubble operations)
- **solution_heapq.py**: O(log n) insert and delete using Python's built-in `heapq` module — the idiomatic Python approach
