"""Doubly Linked List Template - Starter code for implementation.

This template provides the structure for a doubly linked list with
bidirectional traversal: insert, delete, search, and traverse operations.

Key feature: Navigate both forward and backward through the list!

Time Complexity:
    - insert: O(1) at tail (if tail pointer maintained)
    - delete: O(n) average case
    - search: O(n)
    - traverse_forward: O(n)
    - traverse_backward: O(n)

Space Complexity: O(n) for n nodes (extra pointer per node)
"""

from typing import List


class Node:
    """Represents a single node in the doubly linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Solution:
    """Doubly Linked List with bidirectional traversal."""

    def __init__(self):
        """Initialize an empty doubly linked list."""
        raise NotImplementedError("Initialize head and tail pointers")

    def insert(self, value) -> None:
        """Insert a value at the end of the doubly linked list.

        Args:
            value: The value to insert
        """
        raise NotImplementedError("Implement insert operation")

    def delete(self, value) -> None:
        """Delete the first occurrence of a value from the list.

        Args:
            value: The value to delete
        """
        raise NotImplementedError("Implement delete operation")

    def search(self, value) -> bool:
        """Search for a value in the doubly linked list.

        Args:
            value: The value to search for

        Returns:
            True if value found, False otherwise
        """
        raise NotImplementedError("Implement search operation")

    def traverse_forward(self) -> List:
        """Traverse the list from head to tail.

        Returns:
            List of all values in forward order
        """
        raise NotImplementedError("Implement forward traversal")

    def traverse_backward(self) -> List:
        """Traverse the list from tail to head.

        Returns:
            List of all values in reverse order
        """
        raise NotImplementedError("Implement backward traversal")
