# Algorithm Analysis – Linked List Length Parity

## Approach: Single-Bit Toggle (O(1) Space)

### Algorithm Steps

1. Start with `count = 0` and `current = self.head`.
2. For every node: `count = (count + 1) % 2`.
   - After an **odd** number of steps, `count = 1`.
   - After an **even** number of steps, `count = 0`.
3. Return `"Even"` if `count == 0`, else `"Odd"`.

```
List:  A → B → C → None

Step 1: count=(0+1)%2=1   ("Odd" so far)
Step 2: count=(1+1)%2=0   ("Even" so far)
Step 3: count=(0+1)%2=1   ("Odd" so far)
Stop  → return "Odd"   ✓ (3 elements)
```

### Complexity

| Metric | Value | Reason |
|---|---|---|
| Time | O(n) | One traversal through all n nodes |
| Space | O(1) | Only a single integer toggled between 0 and 1 |

### Why Toggle Instead of Count?

A naive approach stores the full count (`length += 1`) and checks
`length % 2` at the end — O(n) time, O(1) space, identical complexity.

The toggle `(count + 1) % 2` is a micro-optimisation: it avoids integer
growth and makes the intent (parity, not magnitude) explicit in code.

### Comparison of Approaches

| Approach | Time | Space | Notes |
|---|---|---|---|
| Bit toggle (this) | O(n) | O(1) | No integer growth |
| Full counter | O(n) | O(1) | Simple, equally efficient |
| Store all, use `len()` | O(n) | O(n) | Wasteful — never needed |
