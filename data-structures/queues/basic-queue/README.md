# Basic Queue Implementation

## Problem Description

Implement a Queue data structure that follows the "First-In, First-Out" (FIFO) principle using Python's `collections.deque`. The Queue should support the following operations:

1. **enqueue(element)**: Add an element to the end of the queue
2. **dequeue()**: Remove and return the element from the front of the queue
3. **peek()**: Return the element at the front without removing it
4. **is_empty()**: Check if the queue is empty
5. **size()**: Return the number of elements in the queue

## Real-World Analogy

Think of a queue at a grocery store checkout. The person who has been waiting in line the longest (first person) is served first, then the next person, and so on. The last person to join the queue will be the last one to be served.

## Examples

### Example 1: Basic Operations
```python
queue = Solution()
queue.enqueue('Alice')
queue.enqueue('Bob')
queue.enqueue('Charlie')

print(queue.peek())      # Output: 'Alice'
print(queue.dequeue())   # Output: 'Alice'
print(queue.dequeue())   # Output: 'Bob'
print(queue.size())      # Output: 1
print(queue.is_empty())  # Output: False
```

### Example 2: Empty Queue
```python
queue = Solution()
print(queue.is_empty())  # Output: True
print(queue.size())      # Output: 0
```

## Constraints

- Use Python's `collections.deque` for implementation
- Handle edge cases (empty queue operations)
- All operations should be efficient

## Function Signature

```python
from collections import deque

class Solution:
    def __init__(self):
        # Initialize the queue
        pass
    
    def enqueue(self, element):
        # Add element to the end of the queue
        pass
    
    def dequeue(self):
        # Remove and return element from the front
        pass
    
    def peek(self):
        # Return front element without removing
        pass
    
    def is_empty(self):
        # Check if queue is empty
        pass
    
    def size(self):
        # Return number of elements
        pass
```

## Notes

- The deque (double-ended queue) provides O(1) time complexity for both append and popleft operations
- This makes it ideal for implementing queues in Python
- Regular Python lists have O(n) time complexity for pop(0), making them less efficient
