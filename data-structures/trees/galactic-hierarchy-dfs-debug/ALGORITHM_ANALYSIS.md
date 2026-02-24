# Algorithm Analysis: Galactic Hierarchy DFS — Debugging Infinite Recursion

## The Bug Explained

The original code contains a single-character mistake with catastrophic consequences:

```python
# BUGGY
for child in self.children:
    self.depth_first_search()   # ← calls DFS on self, not child!

# FIXED
for child in self.children:
    child.depth_first_search()  # ← calls DFS on child ✓
```

### Why it causes infinite recursion

When the loop runs on the root node:

- It iterates over `self.children` (e.g. `[Left Child, Right Child]`)
- But instead of calling DFS on each `child`, it calls `self.depth_first_search()` — i.e. DFS on **Root** again
- This creates an unbounded recursive call: Root → Root → Root → … → `RecursionError`

The `child` loop variable is never used at all, making the iteration pointless.

## The Fix

```python
def depth_first_search(self, result=None):
    if result is None:
        result = []
    result.append(self.value)
    for child in self.children:
        child.depth_first_search(result)  # delegate to child, not self
    return result
```

## Corrected Traversal

Starting from `Root`:

```
Root → Left Child → Left Grandchild → Right Grandchild → Right Child
```

| Step | Node visited | Reason |
|------|--------------|--------|
| 1 | Root | Starting node |
| 2 | Left Child | First child of Root |
| 3 | Left Grandchild | First child of Left Child |
| 4 | Right Grandchild | Second child of Left Child |
| 5 | Right Child | Second child of Root (backtrack) |

## Complexity Analysis

| Measure | Value | Reasoning |
|---------|-------|-----------|
| **Time** | **O(n)** | Each node visited exactly once |
| **Space** | **O(h)** | Call stack depth equals tree height `h` |

- This tree has width 2 and height 3 → stack depth ≤ 3 frames.

## Key Debugging Lesson

> **Always verify that recursion delegates to the correct object.**
> In a loop over children, the recursive call must be `child.method()`, not `self.method()`.
> Using `self` re-processes the current node endlessly; using `child` advances the traversal.
