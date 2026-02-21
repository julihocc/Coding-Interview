"""Linked List – Length: Iterative Solution.

Algorithm
---------
Start a counter at 0, then walk from head to None, incrementing the
counter for every node visited. Return the counter.

Time Complexity : O(n) – visits every node once
Space Complexity: O(1) – only a single integer counter
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
        """Prepend a node (insert at the front) – O(1)."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def LinkedList_length(self) -> int:
        """Return the number of nodes in the linked list – O(n)."""
        current_node = self.head
        length = 0
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length

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


# ── Demo ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    queue = Solution()
    queue.push("Alice")
    queue.push("Bob")
    queue.push("Carol")
    print("List:", queue.to_list())
    print("Length:", queue.LinkedList_length())   # 3
