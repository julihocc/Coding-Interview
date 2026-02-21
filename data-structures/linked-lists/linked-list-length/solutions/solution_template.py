"""Linked List – Length: Starter / Template.

Your task
---------
Implement ``LinkedList_length`` so that it returns the total number of
nodes in the linked list.

Call-center scenario
--------------------
    queue.push("Alice")
    queue.push("Bob")
    queue.push("Carol")
    print(queue.LinkedList_length())   # Expected: 3

Hint
----
1. Set a counter to 0 and start at self.head.
2. While the current node is not None, increment the counter and advance.
3. Return the counter.
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

    def LinkedList_length(self) -> int:
        """Return the number of nodes in the linked list."""
        raise NotImplementedError("Implement LinkedList_length")

    def to_list(self) -> List:
        """Return all node values as a Python list (utility)."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def print_list(self) -> None:
        """Print the list head-to-tail in the format: A->B->C->"""
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print()


# ── Demo (matches the problem statement) ────────────────────────────────────
if __name__ == "__main__":
    queue = Solution()
    queue.push("Alice")
    queue.push("Bob")
    queue.push("Carol")
    print(queue.LinkedList_length())   # Expected: 3
