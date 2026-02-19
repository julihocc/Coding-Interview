"""Doubly Linked List - Optimized Implementation.

This implementation maintains both head and tail pointers for O(1) insertions
and O(1) backward traversal start point.

Time Complexity:
    - insert: O(1) with tail pointer
    - delete: O(n) - must still traverse
    - search: O(n)
    - traverse_forward: O(n)
    - traverse_backward: O(n)

Space Complexity: O(n)
"""

from typing import List


class Node:
    """Represents a single node in the doubly linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Solution:
    """Doubly Linked List implementation with head and tail pointers."""

    def __init__(self):
        """Initialize an empty doubly linked list."""
        self.head = None
        self.tail = None

    def insert(self, value) -> None:
        """Insert a value at the end of the doubly linked list.

        Time: O(1) constant time with tail pointer
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, value) -> None:
        """Delete the first occurrence of a value from the list.

        Time: O(n) - must traverse to find node
        """
        current = self.head

        while current is not None:
            if current.value == value:
                # Handle deletion
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    # Deleting head
                    self.head = current.next

                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    # Deleting tail
                    self.tail = current.prev

                return

            current = current.next

    def search(self, value) -> bool:
        """Search for a value in the doubly linked list.

        Time: O(n)
        """
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next

        return False

    def traverse_forward(self) -> List:
        """Traverse the list from head to tail.

        Time: O(n)
        """
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next

        return result

    def traverse_backward(self) -> List:
        """Traverse the list from tail to head.

        Time: O(n)
        Efficient with tail pointer - no need to find tail first
        """
        result = []
        current = self.tail
        while current is not None:
            result.append(current.value)
            current = current.prev

        return result
