# Min Stack

## Problem Statement

Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in **constant time** $O(1)$.

## Problem Description

Implement a `MinStack` class with the following operations:

- `push(x: int)`: Push element x onto the stack
- `pop()`: Remove the element on top of the stack
- `top()`: Get the top element
- `get_min()`: Retrieve the minimum element in the stack

**Critical Requirement:** All operations, including `get_min()`, must run in $O(1)$ time complexity.

## Examples

### Example 1: Basic Operations
```python
stack = MinStack()
stack.push(5)
stack.push(2)
stack.push(4)
stack.get_min()  # Returns 2
stack.pop()      # Removes 4
stack.top()      # Returns 2
stack.get_min()  # Returns 2
```

### Example 2: Tracking Minimum Changes
```python
stack = MinStack()
stack.push(3)
stack.get_min()  # Returns 3
stack.push(2)
stack.get_min()  # Returns 2
stack.push(1)
stack.get_min()  # Returns 1
stack.pop()      # Removes 1
stack.get_min()  # Returns 2 (updates correctly)
```

### Example 3: Duplicate Minimums
```python
stack = MinStack()
stack.push(2)
stack.push(2)
stack.push(2)
stack.get_min()  # Returns 2
stack.pop()
stack.get_min()  # Still returns 2
```

## Real-World Applications

### Financial Trading Systems
In high-frequency trading, you need to:
- Track current orders (stack operations)
- Instantly know the lowest price in your order book
- Make decisions in microseconds

### Resource Management
System resource monitoring where you:
- Add/remove resource usage measurements
- Always know the minimum available resource
- Need instant access without scanning all data

### Paper Stack with Values
Imagine managing a physical stack of papers, each with a number:
- You can add papers on top
- You can remove the top paper
- You need to instantly know which paper has the smallest number
- Scanning all papers each time is too slow!

## Constraints

- Values can be positive, negative, or zero
- Stack can be empty (return `None` for operations on empty stack)
- Number of operations: $1 \leq n \leq 10^5$
- Value range: $-10^9 \leq x \leq 10^9$

## Function Signatures

```python
class Solution:
    def __init__(self):
        """Initialize the data structure."""
        pass
    
    def push(self, x: int) -> None:
        """Push element x onto stack."""
        pass
    
    def pop(self) -> None:
        """Remove the element on top of the stack."""
        pass
    
    def top(self) -> Optional[int]:
        """Get the top element."""
        pass
    
    def get_min(self) -> Optional[int]:
        """Retrieve the minimum element in O(1) time."""
        pass
```

## Time and Space Complexity Goals

### Naive Approach
- `push()`: $O(1)$
- `pop()`: $O(1)$
- `top()`: $O(1)$
- `get_min()`: $O(n)$ ❌ (scans entire stack)

### Optimized Approach
- `push()`: $O(1)$ ✓
- `pop()`: $O(1)$ ✓
- `top()`: $O(1)$ ✓
- `get_min()`: $O(1)$ ✓
- **Space**: $O(n)$ (auxiliary space for tracking minimums)

## Key Insights

1. **The Challenge**: How to track minimum without scanning the entire stack?
2. **The Solution**: Use an auxiliary structure to maintain minimum information
3. **The Trick**: Keep minimum history that updates as elements are pushed/popped

See [ALGORITHM_ANALYSIS.md](ALGORITHM_ANALYSIS.md) for detailed algorithm explanations and complexity analysis.
