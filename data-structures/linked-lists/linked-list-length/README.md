# Linked List – Length

## Problem Statement

You manage a **call center queue** represented as a singly linked list.
Each node holds a pending caller. Your task is to find **how many callers**
are in the queue — i.e., the length of the linked list.

### Starter Code

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        """Prepend a node (inserts at the front)."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # TODO: implement this method
    def LinkedList_length(self):
        ...

queue = LinkedList()
queue.push("Alice")
queue.push("Bob")
queue.push("Carol")
print(queue.LinkedList_length())   # Expected: 3
```

### Operations to Implement

| Method | Description |
|---|---|
| `push(data)` | Prepend – inserts at the front *(already provided)* |
| `LinkedList_length()` | Return the **count of nodes** in the list |

> **Note:** Python's built-in `len()` only works on built-in types such as
> `list` or `str`. It cannot measure the length of a custom linked list.

### Edge Cases

| Scenario | Expected Behaviour |
|---|---|
| Empty list | Returns `0` |
| Single node | Returns `1` |
| Multiple nodes | Returns exact node count |

## Key Concept

Walk from `head` to `None`, incrementing a counter for every node visited:

```python
def LinkedList_length(self):
    current_node = self.head
    length = 0
    while current_node is not None:
        length += 1
        current_node = current_node.next
    return length
```

**Time Complexity:** O(n) — visits every node once  
**Space Complexity:** O(1) — only a single integer counter is needed
