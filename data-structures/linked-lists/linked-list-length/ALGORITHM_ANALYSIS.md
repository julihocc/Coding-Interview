# Algorithm Analysis – Linked List Length

## Approach: Iterative Counter

### Algorithm Steps

1. Set `current_node = self.head` and `length = 0`.
2. While `current_node` is not `None`:
   - Increment `length`.
   - Advance `current_node = current_node.next`.
3. Return `length`.

```
List:  A → B → C → None

Step 1: current=A, length=1
Step 2: current=B, length=2
Step 3: current=C, length=3
Step 4: current=None → stop, return 3
```

### Complexity

| Metric | Value | Reason |
|---|---|---|
| Time | O(n) | Visits each of the n nodes exactly once |
| Space | O(1) | Only a counter integer — no extra data structures |

### Why Not Use `len()`?

Python's `len()` is implemented for types that define `__len__`. A custom
`LinkedList` class does not define `__len__` by default, so calling `len(llist)`
would raise a `TypeError`. You would need to either implement `__len__` (which
itself requires a traversal) or use the iterative approach above.

### Alternative: Recursive Counter

```python
def _count(self, node):
    if node is None:
        return 0
    return 1 + self._count(node.next)
```

| Approach | Time | Space |
|---|---|---|
| Iterative | O(n) | O(1) |
| Recursive | O(n) | O(n) call stack |

The iterative approach is preferred because it avoids Python's recursion limit
for very long lists and uses constant space.
