# Linked List Implementation

## Problem Statement

Implement a singly linked list data structure with the following operations:

### Node Structure
A basic node with a value and a reference to the next node:
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

### Operations to Implement

1. **`insert(value: int) -> None`**
   - Insert a value at the end of the linked list
   - If the list is empty, the new node becomes the head

2. **`delete(value: int) -> None`**
   - Delete the first occurrence of a node with the given value
   - If the value is not found, do nothing
   - Handle deletion of head node properly

3. **`search(value: int) -> bool`**
   - Return `True` if the value exists in the list, `False` otherwise

4. **`to_list() -> List[int]`**
   - Return a list of all values in the linked list in order
   - Useful for testing and validation

### Example Usage

```python
ll = Solution()
ll.insert(1)
ll.insert(2)
ll.insert(3)
print(ll.to_list())  # [1, 2, 3]

ll.delete(2)
print(ll.to_list())  # [1, 3]

print(ll.search(3))  # True
print(ll.search(5))  # False
```

## Key Concepts

- **Sequential storage** via node links
- **Dynamic insertion/deletion** at O(1) after finding position
- **Linear traversal** required for search
- **Head/tail tracking** for efficient operations
