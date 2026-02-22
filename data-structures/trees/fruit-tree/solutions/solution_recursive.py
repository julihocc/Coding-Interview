"""Recursive solution for Fruit Tree — Insert Node and Pre-Order Traversal.

Phase 1: DFS to find "Pear".
Phase 2: add_child("Plum") onto the found node.
Phase 3: Pre-order traversal (the lesson's print_tree, returning a list).
"""
from typing import Optional


class TreeNode:
    """A node in the fruit tree."""
    def __init__(self, value: str):
        self.value = value
        self.children: list["TreeNode"] = []

    def add_child(self, child_node: "TreeNode") -> None:
        self.children.append(child_node)

    def remove_child(self, child_node: "TreeNode") -> None:
        self.children = [c for c in self.children if c is not child_node]


class Solution:
    # ------------------------------------------------------------------ #
    #  Helper: DFS Search                                                  #
    # ------------------------------------------------------------------ #
    def _find(self, node: Optional[TreeNode], target: str) -> Optional[TreeNode]:
        """Return the first node whose value equals `target`, or None.

        Time Complexity:  O(n)
        Space Complexity: O(h)
        """
        if node is None:
            return None
        if node.value == target:
            return node
        for child in node.children:
            result = self._find(child, target)
            if result is not None:
                return result
        return None

    # ------------------------------------------------------------------ #
    #  Helper: Pre-Order Traversal (print_tree equivalent)                 #
    # ------------------------------------------------------------------ #
    def _pre_order(self, node: Optional[TreeNode], result: list[str]) -> None:
        """Append node values in pre-order (root → children).

        Time Complexity:  O(n)
        Space Complexity: O(h)
        """
        if node is None:
            return
        result.append(node.value)
        for child in node.children:
            self._pre_order(child, result)

    # ------------------------------------------------------------------ #
    #  Main Method                                                         #
    # ------------------------------------------------------------------ #
    def insert_and_traverse(self, root: Optional[TreeNode]) -> list[str]:
        """Insert Plum under Pear, then return pre-order traversal.

        Time Complexity:  O(n) — one DFS search + one traversal.
        Space Complexity: O(h) — recursion depth for both phases.
        """
        if root is None:
            return []

        # Phase 1: Find "Pear"
        pear = self._find(root, "Pear")

        # Phase 2: Insert "Plum" (only if Pear exists)
        if pear is not None:
            pear.add_child(TreeNode("Plum"))

        # Phase 3: Pre-order traversal of the (possibly updated) tree
        result: list[str] = []
        self._pre_order(root, result)
        return result
