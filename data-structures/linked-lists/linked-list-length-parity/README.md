# Linked List – Length Parity

## Problem Statement

Given a singly linked list, determine whether the number of elements is
**even** or **odd** — without storing the full count.

Return `"Even"` if the list has an even number of elements, `"Odd"` otherwise.
An empty list has 0 elements, which is **even**.

### Starter Code

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # TODO: implement this method
    def length_parity(self):
        ...
```

### Example

```python
ll = LinkedList()
ll.add_node(1); ll.add_node(2); ll.add_node(3)
ll.length_parity()   # "Odd"

ll2 = LinkedList()
ll2.add_node(10); ll2.add_node(20); ll2.add_node(30); ll2.add_node(40)
ll2.length_parity()  # "Even"

ll3 = LinkedList()
ll3.length_parity()  # "Even"  (empty → 0 elements)
```

### Operations to Implement

| Method | Description |
|---|---|
| `add_node(data)` | Append a node at the tail *(already provided)* |
| `length_parity()` | Return `"Even"` or `"Odd"` |

### Edge Cases

| Scenario | Expected |
|---|---|
| Empty list | `"Even"` |
| 1 element | `"Odd"` |
| Even count | `"Even"` |
| Odd count | `"Odd"` |

## Key Concept

Toggle a single bit instead of accumulating a full count — O(1) space:

```python
def length_parity(self):
    current = self.head
    count = 0
    while current:
        count = (count + 1) % 2   # flips between 0 and 1
        current = current.next
    return "Even" if count == 0 else "Odd"
```

`count` is always 0 (even number of nodes seen so far) or 1 (odd).

**Time Complexity:** O(n)  
**Space Complexity:** O(1)
