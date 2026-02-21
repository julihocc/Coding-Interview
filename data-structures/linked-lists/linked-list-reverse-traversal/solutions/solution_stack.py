"""Linked List – Reverse Traversal: Stack-Based Solution.

Algorithm
---------
1. Forward pass: traverse head → tail, pushing each value onto a stack.
2. Reverse pass: pop all values from the stack (LIFO gives tail → head order).

Time Complexity : O(n) – two linear passes
Space Complexity: O(n) – stack holds all n values
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

    def LinkedList_reverseTraversal(self) -> None:
        """Print each element from tail to head using a stack."""
        node = self.head
        stack = []
        while node is not None:
            stack.append(node.data)
            node = node.next
        while stack:
            print(stack.pop())

    def to_reverse_list(self) -> List:
        """Return elements tail-to-head as a Python list (used by the judge)."""
        node = self.head
        stack = []
        while node is not None:
            stack.append(node.data)
            node = node.next
        result = []
        while stack:
            result.append(stack.pop())
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
    llist = Solution()
    llist.push("youtube.com")
    llist.push("github.com")
    llist.push("google.com")
    # list: google.com -> github.com -> youtube.com
    print("Forward order:")
    llist.print_list()
    print("Reverse order:")
    llist.LinkedList_reverseTraversal()
