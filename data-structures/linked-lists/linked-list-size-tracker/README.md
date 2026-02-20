# Linked List Size Tracker — Debugging Challenge

## Problem Statement

A `size` property has been added to the `LinkedList` class to track the number of nodes.
However, a bug has crept in — `size` doesn't update correctly when nodes are inserted or removed.

Your mission: **find and fix the bug** so that `size` always reflects the true number of nodes.

### Buggy Starter Code

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
        self.size += 1          # ← looks right…

    def delete(self, data):
        temp = self.head
        prev = None
        while temp:
            if temp.data == data:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                self.size += 1  # ← BUG IS HERE
                return
            prev = temp
            temp = temp.next
```

### Expected Behaviour

```python
ll = LinkedList()
ll.insert(1); ll.insert(2); ll.insert(3)
print(ll.size)    # 3

ll.delete(2)
print(ll.size)    # 2  ← buggy code prints 4 instead!

ll.delete(5)      # non-existent node – size must not change
print(ll.size)    # 2
```

### Operations

| Method | Description |
|---|---|
| `insert(data)` | Append a new node at the tail; `size += 1` |
| `delete(data)` | Remove first occurrence; `size -= 1` only if found |
| `to_list()` | Return all values as a Python list |
| `size` (property) | Always equals the number of nodes currently in the list |

## The Bug

Inside `delete`, the line that updates `size` reads:

```python
self.size += 1   # wrong – should subtract, not add
```

**Fix:** Change `+= 1` to `-= 1`.

## Key Lessons

- Always double-check **increment vs decrement** in counter updates
- The bug only manifests on **delete** — insert was already correct
- Deleting a **non-existent** node must **not** change `size` (the return
  before the size line already handles this correctly once the sign is fixed)
