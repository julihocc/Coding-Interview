"""Circular Linked List - Naive Implementation.

This implementation covers the basic operations with straightforward logic.
Good for understanding fundamentals. Traverses to tail each insertion.

Time Complexity:
    - insert: O(n) - traverse to find tail each time
    - delete: O(n) - traverse to find and delete
    - search: O(n) - linear search around cycle
    - to_list: O(n)

Space Complexity: O(n)
"""

from typing import List


class Node:
    """Represents a single node in the circular linked list."""

    def __init__(self, value: int):
        self.value = value
        self.next = None


class Solution:
    """Circular Linked List implementation."""

    def __init__(self):
        """Initialize an empty circular linked list."""
        self.head = None

    def insert(self, value: int) -> None:
        """Insert a value at the end of the circular linked list.

        Time: O(n) because we traverse to find the end
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node  # Point to itself
            return

        # Traverse to find the last node
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head  # Maintain circularity

    def delete(self, value: int) -> None:
        """Delete the first occurrence of a value from the list.

        Time: O(n) worst case
        """
        if self.head is None:
            return

        # Check if head needs to be deleted
        if self.head.value == value:
            if self.head.next == self.head:
                # Only one node
                self.head = None
            else:
                # Find last node and update its next
                last = self.head
                while last.next != self.head:
                    last = last.next
                last.next = self.head.next
                self.head = self.head.next
            return

        # Traverse to find and delete
        current = self.head
        while current.next != self.head:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def search(self, value: int) -> bool:
        """Search for a value in the circular linked list.

        Time: O(n)
        """
        if self.head is None:
            return False

        current = self.head
        while True:
            if current.value == value:
                return True
            current = current.next
            if current == self.head:
                break

        return False

    def to_list(self) -> List[int]:
        """Convert the circular linked list to a Python list.

        Time: O(n)
        """
        if self.head is None:
            return []

        result = []
        current = self.head
        while True:
            result.append(current.value)
            current = current.next
            if current == self.head:
                break

        return result
