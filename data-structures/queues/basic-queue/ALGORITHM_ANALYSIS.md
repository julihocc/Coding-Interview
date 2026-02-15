# Algorithm Analysis: Basic Queue

## Overview

A Queue is a linear data structure that follows the First-In, First-Out (FIFO) principle. Elements are added at the rear (enqueue) and removed from the front (dequeue).

## Implementation Approaches

### Approach 1: Using Python List (Naive)

**Description**: Use a Python list with `append()` for enqueue and `pop(0)` for dequeue.

**Time Complexity**:
- `enqueue(element)`: O(1) - appending to the end of a list
- `dequeue()`: O(n) - removing from the front requires shifting all elements
- `peek()`: O(1) - accessing the first element
- `is_empty()`: O(1) - checking list length
- `size()`: O(1) - returning list length

**Space Complexity**: O(n) where n is the number of elements in the queue

**Drawback**: The O(n) dequeue operation makes this approach inefficient for frequent removals.

### Approach 2: Using collections.deque (Optimized)

**Description**: Use Python's `collections.deque` which is implemented as a doubly-linked list, providing O(1) operations at both ends.

**Time Complexity**:
- `enqueue(element)`: O(1) - appending to the end
- `dequeue()`: O(1) - removing from the front
- `peek()`: O(1) - accessing the first element
- `is_empty()`: O(1) - checking deque length
- `size()`: O(1) - returning deque length

**Space Complexity**: O(n) where n is the number of elements in the queue

**Advantages**: 
- All operations are O(1)
- Efficient memory usage
- Built-in Python module
- Thread-safe for append and pop operations from opposite ends

## Why deque Over List?

The key difference is in the dequeue operation:

```python
# List implementation - O(n)
queue_list = []
queue_list.append(1)  # O(1)
queue_list.pop(0)     # O(n) - shifts all elements

# Deque implementation - O(1)
from collections import deque
queue_deque = deque()
queue_deque.append(1)    # O(1)
queue_deque.popleft()    # O(1) - no shifting needed
```

## Practical Applications

1. **Task Scheduling**: Managing tasks in the order they arrive
2. **Printer Queue**: Processing print jobs in sequence
3. **Breadth-First Search (BFS)**: Graph traversal algorithm
4. **Message Queues**: Processing messages in distributed systems
5. **Call Center Systems**: Handling customer calls in order

## Comparison with Other Data Structures

| Operation | Queue (deque) | Stack | Array/List |
|-----------|---------------|-------|------------|
| Insert    | O(1)          | O(1)  | O(1)*      |
| Delete    | O(1)          | O(1)  | O(n)       |
| Access    | O(1) (front)  | O(1)  | O(1)       |
| Search    | O(n)          | O(n)  | O(n)       |

*Amortized time for dynamic arrays

## Best Practices

1. Always use `collections.deque` for queue implementation in Python
2. Handle empty queue cases with appropriate error handling
3. Use `is_empty()` before dequeue/peek operations to avoid errors
4. Consider thread-safety requirements for concurrent applications
