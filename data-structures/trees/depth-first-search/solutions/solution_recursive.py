"""Recursive DFS solution for tree traversal and path finding.

Implements:
  - dfs()       : full depth-first traversal starting from a root node.
  - find_path() : DFS-based path discovery between two nodes.

The tree is represented as a bidirectional adjacency dictionary.
A `visited` set is used to avoid revisiting nodes.
"""


class Solution:
    def dfs(self, tree: dict, root: str) -> list[str]:
        """Return all nodes reachable from root in DFS order.

        Time Complexity:  O(V) — each node is visited exactly once (tree: E = V-1).
        Space Complexity: O(V) — visited set + recursion call stack (depth = tree height).
        """
        visited: set[str] = set()
        traversal: list[str] = []

        def _dfs(node: str) -> None:
            traversal.append(node)
            visited.add(node)
            for child in tree[node]:
                if child not in visited:
                    _dfs(child)

        _dfs(root)
        return traversal

    def find_path(self, tree: dict, start: str, end: str) -> list[str] | None:
        """Find a path from start to end using DFS.

        Returns the first path found (not necessarily the shortest),
        or None if no path exists.

        Time Complexity:  O(V) — visits at most all nodes before finding the target.
        Space Complexity: O(V) — visited set + path list + recursion depth.
        """
        visited: set[str] = set()

        def _find(node: str, path: list[str]) -> list[str] | None:
            path = path + [node]
            visited.add(node)
            if node == end:
                return path
            for neighbor in tree[node]:
                if neighbor not in visited:
                    result = _find(neighbor, path)
                    if result:
                        return result
            return None

        return _find(start, [])
