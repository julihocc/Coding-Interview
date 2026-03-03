# MaxHeap

A max-heap data structure implementation.

## Problem

Implement a MaxHeap with the following operations:

- `insert(elt)`: Insert an element (O(log n))
- `delete_max()`: Remove the maximum element (O(log n))
- `max_element()`: Get the maximum element (O(1))
- `size()`: Get the number of elements

## Scenario

Imagine that you are the chief engineer at a space station managing the takeoff queue for spaceships. Spaceships are identified by their license numbers, and the one holding the largest license number initiates takeoff first. You must be able to add spaceships to the queue and remove the one with the largest license number efficiently, especially when sudden technical issues require rescheduling the takeoff sequence.

## Approaches

- **solution_naive.py**: Recursive bubble operations for simplicity
- **solution_optimized.py**: Iterative bubble operations for better performance
- **solution_heapq.py**: O(log n) insert and delete using Python's built-in `heapq` module and value negation — the idiomatic Python workaround for max-heaps
