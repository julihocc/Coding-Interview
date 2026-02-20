"""Doubly Linked List – Backward Display: Starter / Template.

Challenge
---------
The starter code below provides a working DoublyLinkedList with
``insert``, ``delete``, and ``display_forward`` methods.

Your task: implement ``display_backward()`` so that after deleting
'Jupiter' the list is printed from TAIL to HEAD.

Expected output
---------------
    Forward : Mars <-> Saturn <-> END
    Backward: Saturn <-> Mars <-> END

Hints
-----
* Each node already has a ``prev`` pointer – use it!
* Start at ``self.tail`` and follow ``prev`` until you reach ``None``.
"""

from typing import List


# ---------------------------------------------------------------------------
# Node class
# ---------------------------------------------------------------------------
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


# ---------------------------------------------------------------------------
# DoublyLinkedList class  (matches the starter code in the problem statement)
# ---------------------------------------------------------------------------
class Solution:
    """Doubly linked list with forward display (provided) and backward display (your task)."""

    def __init__(self):
        self.head = None
        self.tail = None

    # ------------------------------------------------------------------
    # Insert at tail  –  O(1)  because self.tail is maintained
    # ------------------------------------------------------------------
    def insert(self, data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # ------------------------------------------------------------------
    # Delete first occurrence  –  O(n)
    # ------------------------------------------------------------------
    def delete(self, data) -> None:
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                return
            current_node = current_node.next

    # ------------------------------------------------------------------
    # Forward display (provided – do not modify)
    # ------------------------------------------------------------------
    def display_forward(self) -> List:
        """Traverse head → tail and return values as a list."""
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return result

    # ------------------------------------------------------------------
    # TODO: Implement backward display
    # ------------------------------------------------------------------
    def display_backward(self) -> List:
        """Traverse tail → head and return values as a list.

        Returns:
            List of all values in reverse (tail-to-head) order.
        """
        raise NotImplementedError(
            "Implement display_backward: start at self.tail and follow prev pointers"
        )
