"""Linked List – Insert After Head: Starter / Template.

Your task
---------
Implement the ``insert_after_head`` method so that the new node is
placed immediately after ``self.head``.

Alien network scenario
----------------------
    llist.push("Zog")               # list: Zog
    llist.insert_after_head("Zak")  # list: Zog->Zak
    llist.print_list()              # prints: Zog->Zak->

Hint
----
1. Create the new node.
2. Make the new node point to whatever ``self.head.next`` currently points to.
3. Make ``self.head.next`` point to the new node.
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
        """Prepend a node (insert at the front)."""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_head(self, new_data) -> None:
        """Insert a new node immediately after the current head.

        If the list is empty the new node becomes the head.
        """
        raise NotImplementedError("Implement insert_after_head")

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


# ── Demo (matches the problem statement) ────────────────────────────────────
if __name__ == "__main__":
    llist = Solution()
    llist.push("Zog")
    llist.insert_after_head("Zak")
    llist.print_list()   # Expected: Zog->Zak->
