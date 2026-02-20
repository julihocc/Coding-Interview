"""Doubly Linked List – Backward Display: No-Tail-Pointer Variant.

Purpose
-------
This exists purely as an educational contrast to solution_naive.py.
It intentionally does NOT maintain a ``self.tail`` pointer, so
``display_backward`` must first walk the entire list forward to reach
the end, then walk backward.

Comparison
----------
+--------------------+----------------+---------------------+
| Method             | solution_naive | solution_no_tail    |
+====================+================+=====================+
| insert             | O(1)           | O(n) – find tail    |
| display_backward   | O(n)           | O(2n) – fwd + bwd   |
+--------------------+----------------+---------------------+

Lesson: maintaining a ``tail`` pointer costs one extra reference per
list but makes both insert and backward traversal start instantly,
halving the constant factor of display_backward.

Time Complexity:
    - insert: O(n) – must traverse to find the end
    - delete: O(n)
    - display_forward: O(n)
    - display_backward: O(n) two passes instead of one

Space Complexity: O(n)  — same as the naive solution
"""

from typing import List


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    """Doubly linked list WITHOUT a tail pointer (educational contrast)."""

    def __init__(self):
        self.head = None
        # Intentionally no self.tail

    # ------------------------------------------------------------------
    def insert(self, data) -> None:
        """Insert at the end – O(n) because we must traverse to find it."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        # Walk all the way to the end every time
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        new_node.prev = current

    # ------------------------------------------------------------------
    def delete(self, data) -> None:
        """Delete first occurrence – O(n)."""
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                return
            current = current.next

    # ------------------------------------------------------------------
    def display_forward(self) -> List:
        """Traverse head → tail – O(n)."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    # ------------------------------------------------------------------
    def display_backward(self) -> List:
        """Traverse tail → head – O(n) but requires TWO passes.

        Pass 1 (forward): walk from head to find the tail.
        Pass 2 (backward): walk from tail back to head using prev pointers.

        Without self.tail we have no shortcut — we must discover the
        tail on every call.
        """
        if self.head is None:
            return []

        # Pass 1 – find the tail the slow way
        current = self.head
        while current.next is not None:
            current = current.next

        # Pass 2 – walk backwards from the tail we just found
        result = []
        while current is not None:
            result.append(current.data)
            current = current.prev
        return result
