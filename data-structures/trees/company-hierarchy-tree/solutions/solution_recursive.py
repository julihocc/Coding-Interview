"""Recursive solution for Company Hierarchy Tree — Restructure and Traverse.

Approach:
  Phase 1 — DFS search to locate target nodes.
  Phase 2 — Rewire the tree using add_child / remove_child.
  Phase 3 — Pre-order DFS to collect the final traversal.
"""
from typing import Optional


class TreeNode:
    """A node in the company hierarchy tree."""
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

        Time Complexity:  O(n) in the worst case.
        Space Complexity: O(h), where h is the tree height.
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
    #  Helper: Pre-Order Traversal                                         #
    # ------------------------------------------------------------------ #
    def _pre_order(self, node: Optional[TreeNode], result: list[str]) -> None:
        """Append node values to `result` in pre-order (root → children).

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
    def restructure_and_traverse(self, root: Optional[TreeNode]) -> list[str]:
        """Restructure the company tree and return its pre-order traversal.

        Overall Time Complexity:  O(n) — two DFS searches + one traversal.
        Overall Space Complexity: O(h) — recursion depth for all three phases.
        """
        if root is None:
            return []

        # Phase 1: Find the nodes we need to restructure
        vp_engineering = self._find(root, "VP Engineering")
        engineer = self._find(root, "Engineer")

        if vp_engineering is None or engineer is None:
            # Gracefully return traversal if structure doesn't match
            result: list[str] = []
            self._pre_order(root, result)
            return result

        # Phase 2: Rewire the tree
        senior_engineer = TreeNode("Senior Engineer")
        product_manager = TreeNode("Product Manager")

        # Move Engineer from VP Engineering → Senior Engineer
        vp_engineering.remove_child(engineer)     # O(k)
        senior_engineer.add_child(engineer)        # O(1)

        # Attach new nodes to VP Engineering
        vp_engineering.add_child(senior_engineer)  # O(1)
        vp_engineering.add_child(product_manager)  # O(1)

        # Phase 3: Pre-order traversal of the updated tree
        result = []
        self._pre_order(root, result)
        return result
