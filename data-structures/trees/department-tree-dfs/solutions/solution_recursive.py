"""Completed DFS solution for Department Tree Traversal.

Implements the missing recursive loop inside DepartmentTree.traverse():

    for subdept in self.subdepartments:
        if subdept.name not in visited:
            subdept.traverse(visited, result)

The DepartmentTree class uses 'name' and 'subdepartments' instead of
the more common 'value' and 'children', but the DFS logic is identical.
"""

from tests.cases import DepartmentTree


class Solution:
    def dfs(self, root: DepartmentTree) -> list[str]:
        """Return department names in DFS (pre-order) order.

        Time Complexity:  O(n) — every node visited exactly once.
        Space Complexity: O(n) — visited set + result list + O(h) call stack.
        """
        return root.traverse()
