"""Linked List - Naive Implementation.

This implementation covers the basic operations with straightforward logic.
Good for understanding fundamentals.

Time Complexity:
    - insert: O(n) - traverse to find tail each time
    - delete: O(n) - traverse to find and delete
    - search: O(n) - linear search
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
    """Singly Linked List implementation."""

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def insert(self, value: int) -> None:
        """Insert a value at the end of the linked list.

        Time: O(n) because we traverse to find the end
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        # Traverse to find the last node
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def delete(self, value: int) -> None:
        """Delete the first occurrence of a value from the list.

        Time: O(n) worst case
        """
        if self.head is None:
            return

        # Check if head needs to be deleted
        if self.head.value == value:
            self.head = self.head.next
            return

        # Traverse to find and delete
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
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
