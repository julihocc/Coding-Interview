"""Linked List – Insert After Head: Solution.

Algorithm
---------
To insert a new node immediately after the head:

    new_node.next = self.head.next   # splice new node into the chain
    self.head.next = new_node        # head now points to the new node

Edge case: if the list is empty, the new node simply becomes the head
(there is no existing head to insert "after").

Time Complexity: O(1) – no traversal needed, just pointer manipulation
Space Complexity: O(1)
"""

from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def push(self, new_data) -> None:
        """Prepend a node (insert at the front) – O(1)."""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_head(self, new_data) -> None:
        """Insert a new node immediately after the current head – O(1).

        If the list is empty the new node becomes the sole node (head).
        """
        new_node = Node(new_data)

        if self.head is None:
            # Empty list: new node IS the head
            self.head = new_node
            return

        # Splice the new node between head and whatever head pointed to
        new_node.next = self.head.next   # step 1: new node → old second node
        self.head.next = new_node        # step 2: head → new node

    def to_list(self) -> List:
        """Return all node values as a Python list (used by the judge)."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def print_list(self) -> None:
        """Print the list in the format: A->B->C->"""
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print()


# ── Demo ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    llist = Solution()
    llist.push("Zog")
    llist.insert_after_head("Zak")
    llist.print_list()   # Zog->Zak->
