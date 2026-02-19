# Circular Linked List Implementation

## Problem Statement

Implement a circular linked list data structure with the following operations:

### Node Structure
A basic node with a value and a reference to the next node:
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

### Key Difference from Singly Linked List
In a circular linked list, the **last node's `next` pointer points back to the head** instead of being `None`. This creates a cycle, which enables efficient operations like traversal in a loop without checking for `None`.

### Operations to Implement

1. **`insert(value: int) -> None`**
   - Insert a value at the end of the circular linked list
   - If the list is empty, create a single node pointing to itself
   - The last node must always point back to head

2. **`delete(value: int) -> None`**
   - Delete the first occurrence of a node with the given value
   - If the value is not found, do nothing
   - Maintain circularity after deletion
   - Handle deletion when only one node exists

3. **`search(value: int) -> bool`**
   - Return `True` if the value exists in the list, `False` otherwise
   - Stop searching when completing the cycle (back to head)

4. **`to_list() -> List[int]`**
   - Return a list of all values in the circular linked list in order
   - Stop after visiting each node once (don't follow the cycle infinitely)

### Example Usage

```python
cll = Solution()
cll.insert(1)
cll.insert(2)
cll.insert(3)
print(cll.to_list())  # [1, 2, 3]

cll.delete(2)
print(cll.to_list())  # [1, 3]

print(cll.search(3))  # True
print(cll.search(5))  # False
```

## Key Concepts

- **Circular structure**: Last node points to head, not None
- **Cycle detection**: Traversal must track visited nodes or use head as stopping point
- **Insertion**: New nodes inserted at end, must maintain circularity
- **Deletion**: Must handle head deletion differently (update references)
- **Traversal**: Requires stopping condition when returning to head

## Advantages Over Singly Linked List

- No special handling of "end of list" in traversal
- Useful for round-robin scheduling, circular buffers, etc.
- Entire list accessible from any node
