# Linked List – Sum of Every Third Element (Reversed)

## Problem Statement

Given the **head** of a singly linked list, traverse the list from **tail to head**
and return the **sum of every third element** in that reversed order.

> *"Traverse it like a comet — tail to head — and add up every third node you
> pass."* — Cosmo

### Starter Code

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def find_sum(head):
    stack = []
    while head:
        # push each node's value onto the stack
        pass

    sum_, index = 0, 1
    while stack:
        # pop and accumulate every third value
        pass
```

### Example

```
List (head → tail):  1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9

Reversed order:      9  8  7  6  5  4  3  2  1
Positions:           1  2  3  4  5  6  7  8  9
Every 3rd (3,6,9):   7  4  1

Sum = 7 + 4 + 1 = 12
```

### Operations to Implement

| Method | Description |
|---|---|
| `find_sum(head)` | Return sum of every 3rd element in tail-to-head traversal |

### Edge Cases

| Scenario | Expected Behaviour |
|---|---|
| Empty list (`head = None`) | Return `0` |
| Fewer than 3 elements | Return `0` (no 3rd element exists) |
| Exactly 3 elements | Return the value of the tail node |
| Non-multiples of 3 length | Only count nodes at positions 3, 6, 9 … |

## Key Concept

Combine **reverse traversal via a stack** with a **position counter**:

```python
def find_sum(head):
    stack = []
    while head:
        stack.append(head.data)
        head = head.next

    sum_, index = 0, 1
    while stack:
        value = stack.pop()
        if index % 3 == 0:
            sum_ += value
        index += 1
    return sum_
```

**Time Complexity:** O(n)  
**Space Complexity:** O(n) — stack holds all values
