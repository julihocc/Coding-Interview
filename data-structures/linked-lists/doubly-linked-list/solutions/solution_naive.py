"""Doubly Linked List - Naive Implementation.

This implementation covers the basic operations with straightforward logic.
Good for understanding fundamentals. Traverses to tail each insertion.

Time Complexity:
    - insert: O(n) - traverse to find tail each time
    - delete: O(n) - traverse to find and delete
    - search: O(n) - linear search
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
    """Doubly Linked List implementation."""

    def __init__(self):
        """Initialize an empty doubly linked list."""
        self.head = None

    def insert(self, value) -> None:
        """Insert a value at the end of the doubly linked list.

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
        new_node.prev = current

    def delete(self, value) -> None:
        """Delete the first occurrence of a value from the list.

        Time: O(n) worst case
        """
        if self.head is None:
            return

        # Check if head needs to be deleted
        if self.head.value == value:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return

        # Traverse to find and delete
        current = self.head
        while current is not None:
            if current.value == value:
                current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
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
        """
        result = []

        # First, find the tail
        if self.head is None:
            return result

        current = self.head
        while current.next is not None:
            current = current.next

        # Now traverse backward from tail
        while current is not None:
            result.append(current.value)
            current = current.prev

        return result
