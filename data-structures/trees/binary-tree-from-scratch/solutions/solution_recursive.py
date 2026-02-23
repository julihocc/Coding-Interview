"""Recursive solution for Binary Tree From Scratch — Build and Traverse.

Implements all four lesson TODOs, extended with all three traversal orders:
  1. Defines Node class.
  2. Builds a balanced BST with values 1-7.
  3. Implements in-order, pre-order, and post-order traversals.
  4. Returns node values as a list for each traversal type.
"""
from typing import Optional


class Solution:
    # ------------------------------------------------------------------ #
    #  TODO 1: Node class definition                                       #
    # ------------------------------------------------------------------ #
    class Node:
        """A single node in a binary tree."""
        def __init__(self, value: int):
            self.value = value
            self.left:  Optional["Solution.Node"] = None
            self.right: Optional["Solution.Node"] = None

    # ------------------------------------------------------------------ #
    #  Shared: Build the canonical balanced BST                           #
    # ------------------------------------------------------------------ #
    def _build_tree(self) -> "Solution.Node":
        """Build and return the balanced BST shown in README.md.

        Structure:
                4
               / \\
              2   6
             / \\ / \\
            1  3 5  7

        Time Complexity:  O(n) — n pointer assignments.
        Space Complexity: O(n) — n Node objects.
        """
        root = self.Node(4)

        root.left        = self.Node(2)
        root.right       = self.Node(6)

        root.left.left   = self.Node(1)
        root.left.right  = self.Node(3)

        root.right.left  = self.Node(5)
        root.right.right = self.Node(7)

        return root

    # ------------------------------------------------------------------ #
    #  TODO 3a: In-order traversal  (Left → Root → Right)                 #
    # ------------------------------------------------------------------ #
    def _in_order(
        self, node: Optional["Solution.Node"], result: list[int]
    ) -> None:
        """Left → Root → Right. On a BST this yields sorted order.

        Time Complexity:  O(n)
        Space Complexity: O(h) — h = log₂(7) ≈ 3 for this tree.
        """
        if node is None:
            return
        self._in_order(node.left, result)
        result.append(node.value)
        self._in_order(node.right, result)

    # ------------------------------------------------------------------ #
    #  TODO 3b: Pre-order traversal  (Root → Left → Right)                #
    # ------------------------------------------------------------------ #
    def _pre_order(
        self, node: Optional["Solution.Node"], result: list[int]
    ) -> None:
        """Root → Left → Right. Useful for cloning or serialising a tree.

        Time Complexity:  O(n)
        Space Complexity: O(h)
        """
        if node is None:
            return
        result.append(node.value)
        self._pre_order(node.left, result)
        self._pre_order(node.right, result)

    # ------------------------------------------------------------------ #
    #  TODO 3c: Post-order traversal  (Left → Right → Root)               #
    # ------------------------------------------------------------------ #
    def _post_order(
        self, node: Optional["Solution.Node"], result: list[int]
    ) -> None:
        """Left → Right → Root. Useful for deletion or expression eval.

        Time Complexity:  O(n)
        Space Complexity: O(h)
        """
        if node is None:
            return
        self._post_order(node.left, result)
        self._post_order(node.right, result)
        result.append(node.value)

    # ------------------------------------------------------------------ #
    #  Public entry points (one per test case / traversal type)           #
    # ------------------------------------------------------------------ #
    def build_and_inorder(self) -> list[int]:
        """Build the BST and return its in-order traversal → [1,2,3,4,5,6,7]."""
        result: list[int] = []
        self._in_order(self._build_tree(), result)
        return result

    def build_and_preorder(self) -> list[int]:
        """Build the BST and return its pre-order traversal → [4,2,1,3,6,5,7]."""
        result: list[int] = []
        self._pre_order(self._build_tree(), result)
        return result

    def build_and_postorder(self) -> list[int]:
        """Build the BST and return its post-order traversal → [1,3,2,5,7,6,4]."""
        result: list[int] = []
        self._post_order(self._build_tree(), result)
        return result

    # Keep the original name as an alias so existing code still works
    def build_and_traverse(self) -> list[int]:
        """Alias for build_and_inorder (original lesson TODO 4)."""
        return self.build_and_inorder()
