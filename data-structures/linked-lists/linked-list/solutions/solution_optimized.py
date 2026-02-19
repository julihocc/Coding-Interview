"""Linked List - Optimized Implementation.

This implementation maintains a tail pointer for O(1) insertions at the end.
More efficient for insertion-heavy workloads.

Time Complexity:
    - insert: O(1) with tail pointer
    - delete: O(n) - must still traverse
    - search: O(n)
    - to_list: O(n)

Space Complexity: O(n)
"""

from typing import List


class Node:
    """Represents a single node in the linked list."""

    def __init__(self, value: int):
        self.value = value
        self.next = None


class Solution:
    """Singly Linked List implementation with tail pointer optimization."""

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self.tail = None

    def insert(self, value: int) -> None:
        """Insert a value at the end of the linked list.

        Time: O(1) constant time with tail pointer
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, value: int) -> None:
        """Delete the first occurrence of a value from the list.

        Time: O(n) - must traverse to find node
        """
        if self.head is None:
            return

        # Check if head needs to be deleted
        if self.head.value == value:
            self.head = self.head.next
            # If list becomes empty, update tail
            if self.head is None:
                self.tail = None
            return

        # Traverse to find and delete
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                # If we deleted the tail, update tail pointer
                if current.next is None:
                    self.tail = current
                return
            current = current.next

    def search(self, value: int) -> bool:
        """Search for a value in the linked list.

        Time: O(n)
        """
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next

        return False

    def to_list(self) -> List[int]:
        """Convert the linked list to a Python list.

        Time: O(n)
        """
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next

        return result
