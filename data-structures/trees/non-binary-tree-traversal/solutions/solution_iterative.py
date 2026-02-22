"""Iterative BFS solution for Non-Binary Tree Level-Order Traversal.

Uses a queue (collections.deque) to visit nodes level by level.
"""
from collections import deque
from typing import Optional


class Node:
    """A node in a non-binary (multi-way) tree."""
    def __init__(self, value: int):
        self.value = value
        self.children: list["Node"] = []


class Solution:
    def level_order(self, root: Optional[Node]) -> list[int]:
        """Return the level-order (BFS) traversal of the non-binary tree.

        Time Complexity:  O(n) — every node is enqueued and dequeued exactly once.
        Space Complexity: O(w) — the queue holds at most w nodes at a time,
                          where w is the maximum width (nodes at any one level).
                          Worst case O(n) for a flat tree.
        """
        if root is None:
            return []

        result: list[int] = []
        queue: deque[Node] = deque([root])

        while queue:
            node = queue.popleft()
            result.append(node.value)
            for child in node.children:
                queue.append(child)

        return result
