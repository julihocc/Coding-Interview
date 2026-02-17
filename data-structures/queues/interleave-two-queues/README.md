# Interleave Two Queues

## Problem Description

Strap in, astronaut; it's time for an exciting challenge. Imagine you are given two queues of integers. Your task is to create a new queue that interleaves these two input queues.

For instance, if `queue1 = [1, 2, 3, 4, 5]` and `queue2 = [6, 7, 8, 9, 10]`, your new queue should look like this: `[1, 6, 2, 7, 3, 8, 4, 9, 5, 10]`.

### Constraints

-   You should **not modify** the original queues; instead, create a new one.
-   Both queues are guaranteed to be filled with at least one element.
-   Both queues will always be of the same size.

### Function Signature

```python
class Solution:
    def interleave_queues(self, q1: deque, q2: deque) -> deque:
        # Implementation here
```

## Examples

### Example 1
**Input:**
`q1 = [1, 2, 3]`, `q2 = [4, 5, 6]`

**Output:**
`[1, 4, 2, 5, 3, 6]`

### Example 2
**Input:**
`q1 = [10]`, `q2 = [20]`

**Output:**
`[10, 20]`

## Complexity Requirements

-   **Time Complexity**: $O(N)$, where $N$ is the length of the queues.
-   **Space Complexity**: $O(N)$ for the new queue (since we must not modify originals).
