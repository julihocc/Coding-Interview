"""Recursive solution for Binary Tree From Scratch — Build and In-Order Traverse.

Implements all four lesson TODOs:
  1. Defines Node class.
  2. Builds a balanced BST with values 1-7.
  3. Implements recursive in-order traversal.
  4. Returns the sorted list [1, 2, 3, 4, 5, 6, 7].
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
    #  TODO 3: In-order traversal helper                                   #
    # ------------------------------------------------------------------ #
    def _in_order(self, node: Optional[Node], result: list[int]) -> None:
        """Traverse left → root → right, appending values to result.

        Time Complexity:  O(n) — each node visited exactly once.
        Space Complexity: O(h) — call stack depth equals tree height.
                          Here h = log₂(7) ≈ 3, so effectively O(1).
        """
        if node is None:
            return
        self._in_order(node.left, result)    # 1. left subtree
        result.append(node.value)             # 2. current node
        self._in_order(node.right, result)   # 3. right subtree

    # ------------------------------------------------------------------ #
    #  Main method                                                         #
    # ------------------------------------------------------------------ #
    def build_and_traverse(self) -> list[int]:
        """Build a balanced BST and return its in-order traversal.

        Target tree:
                4
               / \\
              2   6
             / \\ / \\
            1  3 5  7

        In-order of a BST = sorted order → [1, 2, 3, 4, 5, 6, 7]

        Time Complexity:  O(n) — construction + traversal both O(n).
        Space Complexity: O(n) — n Node objects + O(h) call stack.
        """
        # TODO 2: Build the binary tree
        root = self.Node(4)

        root.left        = self.Node(2)
        root.right       = self.Node(6)

        root.left.left   = self.Node(1)
        root.left.right  = self.Node(3)

        root.right.left  = self.Node(5)
        root.right.right = self.Node(7)

        # TODO 4: Collect and return the traversal result
        result: list[int] = []
        self._in_order(root, result)
        return result
