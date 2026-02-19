"""Circular Linked List - Optimized Implementation.

This implementation maintains both head and tail pointers for O(1) insertions.
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
    """Represents a single node in the circular linked list."""

    def __init__(self, value: int):
        self.value = value
        self.next = None


class Solution:
    """Circular Linked List implementation with head and tail pointers."""

    def __init__(self):
        """Initialize an empty circular linked list."""
        self.head = None
        self.tail = None

    def insert(self, value: int) -> None:
        """Insert a value at the end of the circular linked list.

        Time: O(1) constant time with tail pointer
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node  # Point to itself
        else:
            self.tail.next = new_node
            new_node.next = self.head  # Maintain circularity
            self.tail = new_node

    def delete(self, value: int) -> None:
        """Delete the first occurrence of a value from the list.

        Time: O(n) - must traverse to find node
        """
        if self.head is None:
            return

        # Check if head needs to be deleted
        if self.head.value == value:
            if self.head == self.tail:
                # Only one node
                self.head = None
                self.tail = None
            else:
                # Update tail's next to new head
                self.tail.next = self.head.next
                self.head = self.head.next
            return

        # Traverse to find and delete
        current = self.head
        while current.next != self.head:
            if current.next.value == value:
                current.next = current.next.next
                # If we deleted the tail, update tail pointer
                if current.next == self.head:
                    self.tail = current
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
