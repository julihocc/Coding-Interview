# Algorithm Analysis: Min Stack

## Problem Overview

Design a stack data structure that supports standard stack operations (`push`, `pop`, `top`) plus a special `get_min()` operation that retrieves the minimum element in **constant time** $O(1)$.

The key challenge: How do we maintain minimum information efficiently as elements are added and removed?

## Approach 1: Naive Solution

### Algorithm

Maintain a single stack for elements. For `get_min()`, scan the entire stack to find the minimum value.

### Implementation

```python
class MinStack:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        if self.stack:
            self.stack.pop()
    
    def top(self):
        return self.stack[-1] if self.stack else None
    
    def get_min(self):
        if not self.stack:
            return None
        return min(self.stack)  # O(n) scan
```

### Complexity Analysis

**Time Complexity:**
- `push(x)`: $O(1)$ - append to list
- `pop()`: $O(1)$ - remove last element
- `top()`: $O(1)$ - access last element
- `get_min()`: $O(n)$ - scan entire stack ❌

**Space Complexity:** $O(n)$ for the stack

### Why It Fails

The $O(n)$ `get_min()` violates the constant-time requirement. For a stack with 10,000 elements, every `get_min()` call would check all 10,000 elements.

## Approach 2: Optimized Solution (Auxiliary Min Stack)

### Key Insight

**Problem:** After popping the minimum element, how do we know the new minimum without rescanning?

**Solution:** Maintain a **parallel stack** that tracks minimum values as they evolve.

**Core Idea:**
- When pushing element `x`, also push `x` onto min-stack if it's ≤ current minimum
- When popping, if we pop the minimum, also pop from min-stack
- The top of min-stack is always the current minimum

### Algorithm

Use two stacks:
1. **Main stack**: Stores all elements
2. **Min stack**: Stores minimum values in parallel

**Invariant:** `min_stack.top()` is always the minimum element in the main stack.

### Pseudocode

```
class MinStack:
    function __init__():
        stack = []
        min_stack = []
    
    function push(x):
        stack.append(x)
        if min_stack is empty OR x <= min_stack.top():
            min_stack.append(x)
    
    function pop():
        if stack is empty:
            return
        if stack.top() == min_stack.top():
            min_stack.pop()
        stack.pop()
    
    function top():
        return stack.top() if stack not empty else None
    
    function get_min():
        return min_stack.top() if min_stack not empty else None
```

### Step-by-Step Example

**Operation Sequence:** `push(5), push(2), push(4), get_min(), pop(), top(), get_min()`

| Step | Operation | Main Stack | Min Stack | Result |
|------|-----------|------------|-----------|--------|
| 1 | `push(5)` | [5] | [5] | - |
| 2 | `push(2)` | [5, 2] | [5, 2] | - |
| 3 | `push(4)` | [5, 2, 4] | [5, 2] | - |
| 4 | `get_min()` | [5, 2, 4] | [5, 2] | **2** |
| 5 | `pop()` | [5, 2] | [5, 2] | - |
| 6 | `top()` | [5, 2] | [5, 2] | **2** |
| 7 | `get_min()` | [5, 2] | [5, 2] | **2** |

**Key Observations:**
- At step 3, we don't push 4 onto min_stack (4 > 2)
- At step 5, we pop only from main stack (4 ≠ 2)
- Min stack correctly maintains minimum information

### Why Duplicate Minimums Matter

**Operation Sequence:** `push(2), push(2), pop(), get_min()`

| Step | Operation | Main Stack | Min Stack | Comment |
|------|-----------|------------|-----------|---------|
| 1 | `push(2)` | [2] | [2] | First 2 |
| 2 | `push(2)` | [2, 2] | [2, 2] | Push duplicate! |
| 3 | `pop()` | [2] | [2] | Pop both stacks (2 == 2) |
| 4 | `get_min()` | [2] | [2] | Still returns 2 ✓ |

**Critical:** The `x <= min_stack[-1]` comparison (not just `<`) ensures we push duplicate minimums. This prevents min_stack from becoming empty prematurely.

### Complexity Analysis

**Time Complexity:**
- `push(x)`: $O(1)$ - two constant-time appends
- `pop()`: $O(1)$ - one or two constant-time pops
- `top()`: $O(1)$ - array access
- `get_min()`: $O(1)$ - array access ✓

**Space Complexity:** $O(n)$
- Main stack: $O(n)$
- Min stack: $O(n)$ worst case (e.g., descending sequence `[5, 4, 3, 2, 1]`)
- Best case min stack: $O(1)$ (e.g., ascending sequence `[1, 2, 3, 4, 5]`)

### Proof of Correctness

**Invariant:** At any point, `min_stack[-1]` equals `min(stack)`.

**Proof by Induction:**

**Base case:** Empty stack → both stacks empty → invariant holds.

**Inductive step:** Assume invariant holds before operation.

1. **Push `x`:**
   - If `x ≤ min_stack[-1]` (or min_stack empty), push `x` onto min_stack
   - New minimum is `min(old_min, x) = x`, which is now `min_stack[-1]` ✓
   - If `x > min_stack[-1]`, don't push → minimum unchanged ✓

2. **Pop:**
   - If `stack[-1] == min_stack[-1]`, pop both
   - The previous minimum (now `min_stack[-1]`) becomes the new minimum ✓
   - If `stack[-1] != min_stack[-1]`, pop only main stack
   - Minimum unchanged, still `min_stack[-1]` ✓

## Comparison

| Aspect | Naive | Optimized |
|--------|-------|-----------|
| `push()` | $O(1)$ | $O(1)$ |
| `pop()` | $O(1)$ | $O(1)$ |
| `top()` | $O(1)$ | $O(1)$ |
| `get_min()` | $O(n)$ ❌ | $O(1)$ ✓ |
| Space | $O(n)$ | $O(n)$ |
| Extra Space | 0 | $O(n)$ (min stack) |

**Trade-off:** We use $O(n)$ extra space to achieve $O(1)$ `get_min()`.

## Edge Cases

1. **Empty stack**: All operations return `None` (or handle gracefully)
2. **Single element**: Min stack contains one element
3. **Descending order** `[5, 4, 3, 2, 1]`: Min stack mirrors main stack
4. **Ascending order** `[1, 2, 3, 4, 5]`: Min stack has only one element `[1]`
5. **All equal** `[5, 5, 5, 5]`: Min stack mirrors main stack
6. **Pop minimum**: Correctly updates to previous minimum
7. **Duplicate minimums**: Handled by `<=` comparison

## Alternative Optimizations

### Space Optimization: Store Differences

Instead of storing actual minimums in min_stack, store differences from current minimum. This can reduce space in some cases but complicates implementation.

**Trade-off:** More complex code vs. marginal space savings (still $O(n)$).

### Single Stack with Pairs

Store `(value, min_at_this_level)` tuples in one stack:

```python
def push(self, x):
    if not self.stack:
        self.stack.append((x, x))
    else:
        current_min = min(x, self.stack[-1][1])
        self.stack.append((x, current_min))
```

**Trade-off:** 
- Simpler conceptually (one stack)
- Always $O(n)$ space (no best case)
- Slightly more memory per element

## Related Problems

- **Max Stack**: Same concept but tracking maximum
- **Min Queue**: Extending to FIFO structure
- **Sliding Window Minimum**: Using deque/monotonic queue
- **Stock Span Problem**: Similar auxiliary structure pattern

## Implementation Notes

- Use `<=` not `<` when comparing for min_stack push (handles duplicates)
- Check for empty stack before accessing `stack[-1]` or `min_stack[-1]`
- Return `None` for operations on empty stack (or raise exception)
- Min stack size is always ≤ main stack size
- Both stacks grow/shrink together (synchronized)
