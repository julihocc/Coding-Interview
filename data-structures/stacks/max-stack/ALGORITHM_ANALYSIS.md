# Algorithm Analysis: Max Stack (Space Rock)

## Problem Overview

Design a stack data structure that supports standard stack operations (`push`, `pop`, `top`) plus a special `get_max()` operation that retrieves the maximum element in **constant time** $O(1)$.

The key challenge: How do we maintain maximum information efficiently as elements are added and removed?

## Approach 1: Naive Solution

### Algorithm

Maintain a single stack for elements. For `get_max()`, scan the entire stack to find the maximum value.

### Implementation

```python
class MaxStack:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        if self.stack:
            self.stack.pop()
    
    def top(self):
        return self.stack[-1] if self.stack else None
    
    def get_max(self):
        if not self.stack:
            return None
        return max(self.stack)  # O(n) scan
```

### Complexity Analysis

**Time Complexity:**
- `push(x)`: $O(1)$
- `pop()`: $O(1)$
- `top()`: $O(1)$
- `get_max()`: $O(n)$ - scan entire stack ❌

**Space Complexity:** $O(n)$ for the stack

### Why It Fails

The $O(n)$ `get_max()` violates the constant-time requirement. For a stack with 10,000 elements, every `get_max()` call would check all 10,000 elements.

## Approach 2: Optimized Solution (Auxiliary Max Stack)

### Key Insight

**Problem:** After popping the maximum element, how do we know the new maximum without rescanning?

**Solution:** Maintain a **parallel stack** that tracks maximum values as they evolve.

**Core Idea:**
- When pushing element `x`, also push `x` onto max-stack if it's `>=` current maximum.
- When popping, if we pop the maximum, also pop from max-stack.
- The top of max-stack is always the current maximum.

### Algorithm

Use two stacks:
1. **Main stack**: Stores all elements
2. **Max stack**: Stores maximum values in parallel

**Invariant:** `max_stack.top()` is always the maximum element in the main stack.

### Pseudocode

```
class MaxStack:
    function __init__():
        stack = []
        max_stack = []
    
    function push(x):
        stack.append(x)
        if max_stack is empty OR x >= max_stack.top():
            max_stack.append(x)
    
    function pop():
        if stack is empty:
            return
        if stack.top() == max_stack.top():
            max_stack.pop()
        stack.pop()
    
    function top():
        return stack.top() if stack not empty else None
    
    function get_max():
        return max_stack.top() if max_stack not empty else None
```

### Step-by-Step Example

**Operation Sequence:** `push(2), push(5), push(3), get_max(), pop(), top(), get_max()`

| Step | Operation | Main Stack | Max Stack | Result |
|------|-----------|------------|-----------|--------|
| 1 | `push(2)` | [2] | [2] | - |
| 2 | `push(5)` | [2, 5] | [2, 5] | - |
| 3 | `push(3)` | [2, 5, 3] | [2, 5] | - |
| 4 | `get_max()` | [2, 5, 3] | [2, 5] | **5** |
| 5 | `pop()` | [2, 5] | [2, 5] | - |
| 6 | `top()` | [2, 5] | [2, 5] | **5** |
| 7 | `get_max()` | [2, 5] | [2, 5] | **5** |

**Key Observations:**
- At step 3, we don't push 3 onto max_stack (3 < 5)
- At step 5, we pop only from main stack (3 ≠ 5)
- Max stack correctly maintains maximum information

### Why Duplicate Maximums Matter

**Operation Sequence:** `push(5), push(5), pop(), get_max()`

| Step | Operation | Main Stack | Max Stack | Comment |
|------|-----------|------------|-----------|---------|
| 1 | `push(5)` | [5] | [5] | First 5 |
| 2 | `push(5)` | [5, 5] | [5, 5] | Push duplicate! |
| 3 | `pop()` | [5] | [5] | Pop both stacks (5 == 5) |
| 4 | `get_max()` | [5] | [5] | Still returns 5 ✓ |

**Critical:** The `x >= max_stack[-1]` comparison (not just `>`) ensures we push duplicate maximums.

### Complexity Analysis

**Time Complexity:**
- `push(x)`: $O(1)$
- `pop()`: $O(1)$
- `top()`: $O(1)$
- `get_max()`: $O(1)$ ✓

**Space Complexity:** $O(n)$
- Main stack: $O(n)$
- Max stack: $O(n)$ worst case (e.g., ascending sequence `[1, 2, 3, 4, 5]`)

### Proof of Correctness

**Invariant:** At any point, `max_stack[-1]` equals `max(stack)`.

**Proof by Induction:**

**Base case:** Empty stack → both stacks empty → invariant holds.

**Inductive step:** Assume invariant holds before operation.

1. **Push `x`:**
   - If `x >= max_stack[-1]` (or max_stack empty), push `x` onto max_stack
   - New maximum is `max(old_max, x) = x`, which is now `max_stack[-1]` ✓
   - If `x < max_stack[-1]`, don't push → maximum unchanged ✓

2. **Pop:**
   - If `stack[-1] == max_stack[-1]`, pop both
   - The previous maximum (now `max_stack[-1]`) becomes the new maximum ✓
   - If `stack[-1] != max_stack[-1]`, pop only main stack
   - Maximum unchanged, still `max_stack[-1]` ✓
