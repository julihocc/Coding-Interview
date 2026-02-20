# Doubly Linked List — Backward Display After Deletion

## Problem Statement

In a doubly linked list, data can flow in **either direction**. The starter code only showcases
forward traversal. Your challenge is to add a `display_backward()` method and demonstrate the
full list state **from tail to head** after removing the node `"Jupiter"`.

### Starter Code

```python
# Node class
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

# DoublyLinkedList class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                return
            current_node = current_node.next

    def display_forward(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print('END')

# Create a doubly linked list
dList = DoublyLinkedList()
dList.insert('Mars')
dList.insert('Jupiter')
dList.insert('Saturn')
dList.delete('Jupiter')
dList.display_forward()   # Mars <-> Saturn <-> END
```

### Operations to Implement

1. **`display_forward() -> None`** *(already provided)*
   - Traverse from `head` to `tail`, printing each node's data

2. **`display_backward() -> None`** *(your task)*
   - Traverse from `tail` to `head`, printing each node's data
   - Use the `prev` pointer that already exists on each node

### Expected Output After Removing `"Jupiter"`

```
Forward : Mars <-> Saturn <-> END
Backward: Saturn <-> Mars <-> END
```

## Key Concepts

- **Bidirectional pointers**: every node holds both `next` and `prev`
- **Tail pointer**: the list maintains `self.tail`, making backward traversal easy — start
  at `self.tail` and follow `prev` pointers until `None`
- **Symmetry**: forward and backward outputs are mirror images of each other

## Hint

```python
def display_backward(self):
    current_node = self.tail        # start at the END
    while current_node:
        print(current_node.data, end=" <-> ")
        current_node = current_node.prev   # walk backwards
    print('END')
```
