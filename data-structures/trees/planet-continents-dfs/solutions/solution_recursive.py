"""Recursive DFS solution for Planet Continents DFS Traversal.

Adds two countries to Africa (Egypt, Kenya) and two to Asia (Japan, South Korea),
then performs DFS traversal using depth_first_search() as a node method.
"""

from tests.cases import Node


class Solution:
    def extend_and_traverse(self, root: Node) -> list[str]:
        """Extend the tree with new countries and return DFS traversal order.

        Time Complexity:  O(n) — every node visited exactly once.
        Space Complexity: O(n) — visited set + result list + O(h) call stack.
        """

        def _find(node: Node, value: str) -> Node | None:
            """Find a direct child of node with the given value."""
            for child in node.children:
                if child.value == value:
                    return child
            return None

        # Locate continents by name (robust regardless of insertion order)
        africa = _find(root, "Africa")
        asia = _find(root, "Asia")

        # Add two more African countries
        if africa:
            africa.add_child("Egypt")
            africa.add_child("Kenya")

        # Add two more Asian countries
        if asia:
            asia.add_child("Japan")
            asia.add_child("South Korea")

        # DFS traversal from root, collecting values into result list
        return root.depth_first_search()
