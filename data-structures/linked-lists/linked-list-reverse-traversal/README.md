# Linked List – Reverse Traversal

## Problem Statement

You are building a **browser history viewer** represented as a singly linked list.
Each node holds a URL. Your task is to traverse the list from **tail to head** and
return all elements in reverse order.

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
    def LinkedList_reverseTraversal(self):
        ...

llist = LinkedList()
llist.push("youtube.com")
llist.push("github.com")
llist.push("google.com")
# list: google.com -> github.com -> youtube.com
llist.LinkedList_reverseTraversal()
# Expected output (one per line):
# youtube.com
# github.com
# google.com
```

### Operations to Implement

| Method | Description |
|---|---|
| `push(data)` | Prepend – inserts at the front *(already provided)* |
| `LinkedList_reverseTraversal()` | Print every element from **tail → head** |
| `to_reverse_list()` | Return reverse order as a Python list *(needed by judge)* |

### Edge Cases

| Scenario | Expected Behaviour |
|---|---|
| Empty list | Nothing is printed; returns `[]` |
| Single node | Prints/returns the single element |
| Multiple nodes | Prints/returns all elements tail-first |

## Key Concept

Because singly linked lists have no backward pointer, we push every node's value
onto a stack (Python list) during a forward pass, then pop them all — which
naturally reverses the order.

```python
def LinkedList_reverseTraversal(self):
    node = self.head
    stack = []
    while node is not None:
        stack.append(node.data)
        node = node.next
    while stack:
        print(stack.pop())
```

**Time Complexity:** O(n) — one forward pass + one pass over the stack  
**Space Complexity:** O(n) — stack holds all n values
