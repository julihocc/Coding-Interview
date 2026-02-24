"""Recursive DFS solution for Company Hierarchy DFS Traversal.

Mirrors the lesson implementation: uses a visited set to guard against
revisiting nodes, and appends each node's value in pre-order (node before children).
"""


class Node:
    """A node in a company hierarchy tree."""

    def __init__(self, value: str):
        self.value = value
        self.children: list["Node"] = []


class Solution:
    def dfs(self, root: Node) -> list[str]:
        """Return department names in DFS (pre-order) traversal order.

        Time Complexity:  O(n) — every node is visited exactly once.
        Space Complexity: O(n) — visited set holds up to n entries;
                          call stack depth equals tree height h (O(h) ≤ O(n)).
        """
        result: list[str] = []
        visited: set[str] = set()

        def _dfs(node: Node) -> None:
            visited.add(node.value)
            result.append(node.value)
            for child in node.children:
                if child.value not in visited:
                    _dfs(child)

        _dfs(root)
        return result
