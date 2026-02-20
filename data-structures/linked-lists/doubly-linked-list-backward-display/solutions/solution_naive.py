"""Doubly Linked List – Backward Display: Naive Solution.

Approach
--------
Walk from ``self.tail`` backward through ``prev`` pointers, collecting
values into a list.  Because the problem's DoublyLinkedList already
maintains a ``tail`` pointer, no extra traversal to find the tail is
needed – the display_backward method runs in O(n) time.

Time Complexity:
    - insert: O(1) – tail pointer is maintained
    - delete: O(n) – linear search to find node
    - display_forward: O(n)
    - display_backward: O(n)

Space Complexity: O(n)
"""

from typing import List


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    """Doubly linked list with both forward and backward display."""

    def __init__(self):
        self.head = None
        self.tail = None

    # ------------------------------------------------------------------
    def insert(self, data) -> None:
        """Insert at tail – O(1)."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # ------------------------------------------------------------------
    def delete(self, data) -> None:
        """Delete first occurrence of data – O(n)."""
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                # Patch the forward link of the previous node
                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev   # deleted node was tail

                # Patch the backward link of the next node
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next   # deleted node was head

                return
            current_node = current_node.next

    # ------------------------------------------------------------------
    def display_forward(self) -> List:
        """Traverse head → tail – O(n)."""
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return result

    # ------------------------------------------------------------------
    def display_backward(self) -> List:
        """Traverse tail → head using prev pointers – O(n).

        Key insight: because self.tail always points to the last node,
        we can start there immediately – no need to traverse forward
        first to find the end.
        """
        result = []
        current_node = self.tail        # start at the END of the list
        while current_node:
            result.append(current_node.data)
            current_node = current_node.prev   # walk backwards
        return result
