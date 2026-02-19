"""Linked List Template - Starter code for implementation.

This template provides the structure for a singly linked list with
basic operations: insert, delete, search, and traversal.

Time Complexity:
    - insert: O(1) at tail (if tail pointer maintained)
    - delete: O(n) average case
    - search: O(n)
    - to_list: O(n)

Space Complexity: O(n) for n nodes
"""

from typing import List


class Node:
    """Represents a single node in the linked list."""

    def __init__(self, value: int):
        self.value = value
        self.next = None


class Solution:
    """Singly Linked List implementation with insert, delete, search operations."""

    def __init__(self):
        """Initialize an empty linked list."""
        raise NotImplementedError("Initialize head and tail pointers")

    def insert(self, value: int) -> None:
        """Insert a value at the end of the linked list.

        Args:
            value: The integer value to insert
        """
        raise NotImplementedError("Implement insert operation")

    def delete(self, value: int) -> None:
        """Delete the first occurrence of a value from the list.

        Args:
            value: The integer value to delete
        """
        raise NotImplementedError("Implement delete operation")

    def search(self, value: int) -> bool:
        """Search for a value in the linked list.

        Args:
            value: The integer value to search for

        Returns:
            True if value found, False otherwise
        """
        raise NotImplementedError("Implement search operation")

    def to_list(self) -> List[int]:
        """Convert the linked list to a Python list.

        Returns:
            List of all values in the linked list in order
        """
        raise NotImplementedError("Implement to_list operation")
