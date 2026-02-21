# Algorithm Analysis – Linked List Reverse Third Sum

## Approach: Stack + Position Counter

### Algorithm Steps

1. **Forward pass** – traverse head → tail, pushing each node's `data` onto a stack.
2. **Reverse pass** – pop values one by one (giving tail → head order).
   Maintain a counter starting at 1. Whenever `counter % 3 == 0`, add the
   value to the running sum.
3. Return the sum.

```
List:   1 → 2 → 3 → 4 → 5 → 6

Stack after push:  [1, 2, 3, 4, 5, 6]

Pop sequence (reversed):
  index=1  value=6  → skip
  index=2  value=5  → skip
  index=3  value=4  → SUM += 4
  index=4  value=3  → skip
  index=5  value=2  → skip
  index=6  value=1  → SUM += 1

SUM = 5
```

### Complexity

| Metric | Value | Reason |
|---|---|---|
| Time | O(n) | One forward pass + one reverse pass, each O(n) |
| Space | O(n) | Stack stores all n node values |

### Could We Do Better on Space?

A **two-pass approach without a stack** would count nodes first (O(n)),
then on a second forward pass visit only nodes at positions
`(n-2), (n-5), (n-8), …` from the head — but that requires knowing n in
advance and is more complex with no real gain.

A **recursive approach** uses the call stack implicitly as O(n) space.

For simplicity and clarity the explicit-stack approach is preferred here.
