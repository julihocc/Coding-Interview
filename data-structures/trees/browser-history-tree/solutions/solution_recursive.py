"""Recursive solution for Browser History Tree — Pre-Order Traversal.

Pre-order: Root → Children (visit current page before its sub-pages).
This directly mirrors the lesson's `print_history` function.
"""
from typing import Optional


class TreeNode:
    """A node in the browser history tree."""
    def __init__(self, value: str):
        self.value = value
        self.children: list["TreeNode"] = []

    def add_child(self, child_node: "TreeNode") -> None:
        self.children.append(child_node)

    def remove_child(self, child_node: "TreeNode") -> None:
        self.children = [c for c in self.children if c is not child_node]


class Solution:
    def pre_order(self, root: Optional[TreeNode]) -> list[str]:
        """Return all visited URLs in pre-order (DFS) traversal.

        Time Complexity:  O(n) — every node is visited exactly once.
        Space Complexity: O(h) — call stack depth equals the tree height h.
                          Worst case (chain): O(n).
                          Best case (flat/wide): O(1).
        """
        result: list[str] = []

        def _traverse(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            result.append(node.value)      # 1. visit current page first
            for child in node.children:    # 2. recurse into each sub-page
                _traverse(child)

        _traverse(root)
        return result
