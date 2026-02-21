"""Linked List – Reverse Traversal: Starter / Template.

Your task
---------
Implement ``LinkedList_reverseTraversal`` so that it prints every element
from tail to head (reverse order).

Also implement ``to_reverse_list`` so the judge can verify your solution.

Browser history scenario
------------------------
    llist.push("youtube.com")
    llist.push("github.com")
    llist.push("google.com")
    # list: google.com -> github.com -> youtube.com
    llist.LinkedList_reverseTraversal()
    # Expected output (one per line):
    # youtube.com
    # github.com
    # google.com

Hint
----
1. Traverse head → tail, pushing every value onto a stack (Python list).
2. Pop all values off the stack — LIFO order gives you tail → head.
"""

from typing import List


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def push(self, data) -> None:
        """Prepend a node (insert at the front)."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def LinkedList_reverseTraversal(self) -> None:
        """Print each element from tail to head."""
        raise NotImplementedError("Implement LinkedList_reverseTraversal")

    def to_reverse_list(self) -> List:
        """Return elements tail-to-head as a Python list (used by the judge)."""
        raise NotImplementedError("Implement to_reverse_list")

    def print_list(self) -> None:
        """Print the list head-to-tail in the format: A->B->C->"""
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print()


# ── Demo (matches the problem statement) ────────────────────────────────────
if __name__ == "__main__":
    llist = Solution()
    llist.push("youtube.com")
    llist.push("github.com")
    llist.push("google.com")
    llist.LinkedList_reverseTraversal()
