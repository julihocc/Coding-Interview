# Linked List – Insert After Head

## Problem Statement

You are building an **alien communication network** represented as a singly linked list.
The network already has a `push` method to prepend nodes, but you need to add an
`insert_after_head` method so that a new node can be placed **immediately after** the
current head.

### Starter Code

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        """Prepend a node (inserts at the front)."""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # TODO: implement this method
    def insert_after_head(self, new_data):
        ...

llist = LinkedList()
llist.push("Zog")
llist.insert_after_head("Zak")
llist.print_list()   # Expected: Zog->Zak->
```

### Operations to Implement

| Method | Description |
|---|---|
| `push(data)` | Prepend – inserts at the front *(already provided)* |
| `insert_after_head(data)` | Insert a new node **right after** the current head |
| `to_list()` | Return all values as a Python list *(needed by judge)* |

### Edge Cases

| Scenario | Expected Behaviour |
|---|---|
| Empty list | Inserting after head of an empty list → the new node becomes the head |
| Single node | New node is appended directly after the existing head |
| Multiple nodes | New node is spliced in between head and the second node |

## Key Concept

`insert_after_head` is a special case of **insert after a given node**:

```python
def insert_after_head(self, new_data):
    new_node = Node(new_data)
    if self.head is None:          # empty list – new node becomes head
        self.head = new_node
        return
    new_node.next = self.head.next # point new node to what head used to point to
    self.head.next = new_node      # head now points to the new node
```
