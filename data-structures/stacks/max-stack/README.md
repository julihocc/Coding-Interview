# Space Rock (Max Stack)

## Problem Statement

Design a stack that supports `push`, `pop`, `top`, and retrieving the maximum element in **constant time** $O(1)$.

## Problem Description

You have to create a step-up version of a stack that not only allows you to add or remove elements but also find out the greatest element in there, all in no time.

Implement a `MaxStack` class with the following operations:

- `push(x: int)`: Like pushing a spaceship into a wormhole, this shoves an element x into your stack.
- `pop()`: Like popping a bubble, this pulls out the top element of the stack.
- `top()`: Lets you sneak a peek at the top element without moving it anywhere.
- `get_max()`: Fetches the giant among all, the maximum element in the stack (the "Space Rock")!

**Critical Requirement:** All operations, including `get_max()`, must run in $O(1)$ time complexity.

## Examples

### Example 1: Basic Operations
```python
stack = MaxStack()
stack.push(1)
stack.push(5)
stack.push(3)
stack.get_max()  # Returns 5
stack.pop()      # Removes 3
stack.top()      # Returns 5
stack.get_max()  # Returns 5
```

### Example 2: Tracking Maximum Changes
```python
stack = MaxStack()
stack.push(2)
stack.get_max()  # Returns 2
stack.push(5)
stack.get_max()  # Returns 5
stack.push(3)
stack.get_max()  # Returns 5
stack.pop()      # Removes 3
stack.pop()      # Removes 5
stack.get_max()  # Returns 2 (updates correctly)
```

## Constraints

- Values can be positive, negative, or zero (integers).
- Stack can be empty (return `None` for operations on empty stack).
- Number of operations: $1 \leq n \leq 10^5$
- Value range: $-10^9 \leq x \leq 10^9$

## Time and Space Complexity Goals

### Naive Approach
- `push()`: $O(1)$
- `pop()`: $O(1)$
- `top()`: $O(1)$
- `get_max()`: $O(n)$ ❌ (scans entire stack)

### Optimized Approach
- `push()`: $O(1)$ ✓
- `pop()`: $O(1)$ ✓
- `top()`: $O(1)$ ✓
- `get_max()`: $O(1)$ ✓
- **Space**: $O(n)$ (auxiliary space for tracking maximums)

See [ALGORITHM_ANALYSIS.md](ALGORITHM_ANALYSIS.md) for detailed algorithm explanations and complexity analysis.
