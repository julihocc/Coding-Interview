# Algorithm Analysis – Linked List Reverse Traversal

## Approach: Stack-Based Reversal

### Algorithm Steps

1. **Forward pass** – traverse from `head` to `tail`, pushing each node's value
   onto a stack (Python list).
2. **Reverse pass** – pop each value from the stack; because a stack is LIFO, the
   last item pushed (the tail) is the first popped.

```
List:   A → B → C → None

Push:   stack = [A, B, C]
Pop:    C, B, A   ← printed / returned in this order
```

### Complexity

| Metric | Value | Reason |
|---|---|---|
| Time | O(n) | Two linear passes: one to build the stack, one to drain it |
| Space | O(n) | Stack holds all n node values simultaneously |

### Why Not Reverse In-Place?

Reversing the pointers would be O(1) space but mutates the list — undesirable when
you only want to *read* the list in reverse. The stack approach is non-destructive.

### Alternative: Recursion

A recursive approach achieves the same effect implicitly (the call stack acts as
the auxiliary stack), but the space complexity is identical — O(n) — and adds
function-call overhead. For large lists it risks a `RecursionError`.

### Trade-offs Summary

| Approach | Time | Space | Mutates List? |
|---|---|---|---|
| Stack (array) | O(n) | O(n) | No |
| Recursion | O(n) | O(n) | No |
| Reverse pointers | O(n) | O(1) | Yes |
