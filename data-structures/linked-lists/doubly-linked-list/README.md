# Doubly Linked List Implementation

## Problem Statement

Implement a doubly linked list data structure with the following operations:

### Node Structure
A node with value, next pointer, and previous pointer:
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
```

### Key Difference from Singly Linked List
In a doubly linked list, each node has **two pointers**: one to the next node and one to the previous node. This enables bidirectional traversal through the list.

### Operations to Implement

1. **`insert(value) -> None`**
   - Insert a value at the end of the doubly linked list
   - If the list is empty, the new node becomes the head and tail
   - Properly maintain both `next` and `prev` pointers

2. **`delete(value) -> None`**
   - Delete the first occurrence of a node with the given value
   - If the value is not found, do nothing
   - Update both forward and backward links after deletion
   - Handle deletion of head, tail, and middle nodes

3. **`search(value) -> bool`**
   - Return `True` if the value exists in the list, `False` otherwise

4. **`traverse_forward() -> List`**
   - Return a list of all values traversing from head to tail

5. **`traverse_backward() -> List`**
   - Return a list of all values traversing from tail to head
   - **Key challenge**: This is the new skill to master!

### Example Usage

```python
dll = Solution()
dll.insert("Mercury")
dll.insert("Venus")
dll.insert("Earth")
dll.insert("Jupiter")
dll.insert("Saturn")

print(dll.traverse_forward())   # ["Mercury", "Venus", "Earth", "Jupiter", "Saturn"]
print(dll.traverse_backward())  # ["Saturn", "Jupiter", "Earth", "Venus", "Mercury"]

dll.delete("Jupiter")
print(dll.traverse_forward())   # ["Mercury", "Venus", "Earth", "Saturn"]
print(dll.traverse_backward())  # ["Saturn", "Earth", "Venus", "Mercury"]
```

## Key Concepts

- **Bidirectional pointers**: Each node maintains links to both next and previous nodes
- **Two-way traversal**: Can navigate forward or backward through the list
- **Symmetrical operations**: Forward and backward traversals must produce mirror results
- **Complex deletion**: Must update both forward and backward links
- **Tail tracking**: Maintains reference to both head and tail for efficient operations

## Advantages Over Singly Linked List

- Traverse backward without reversing the list
- More flexible navigation
- Efficient insertion/deletion at both ends
- Better for algorithms requiring bidirectional search
