"""Recursive solution for Binary Tree In-Order Traversal.

In-order: Left → Root → Right
"""
from typing import Optional


class Node:
    """A node in a binary tree."""
    def __init__(self, value: int):
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class Solution:
    def in_order(self, root: Optional[Node]) -> list[int]:
        """Return the in-order traversal of the binary tree as a list of values.

        Time Complexity:  O(n) — every node is visited exactly once.
        Space Complexity: O(h) — call stack depth equals the tree height h.
                          Best case (balanced): O(log n).
                          Worst case (skewed chain): O(n).
        """
        result: list[int] = []

        def _traverse(node: Optional[Node]) -> None:
            if node is None:
                return
            _traverse(node.left)    # 1. visit left subtree
            result.append(node.value)  # 2. visit current node
            _traverse(node.right)   # 3. visit right subtree

        _traverse(root)
        return result
