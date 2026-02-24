"""Fixed DFS solution for Galactic Hierarchy DFS Debug.

Bug fix: changed self.depth_first_search() → child.depth_first_search()
inside the child loop to correctly delegate traversal to each child node.

Original buggy code:
    for child in self.children:
        self.depth_first_search()   # ← infinite recursion!

Fixed code:
    for child in self.children:
        child.depth_first_search(result)  # ← correct delegation ✓
"""

from tests.cases import TreeNode


class Solution:
    def dfs(self, root: TreeNode) -> list[str]:
        """Return node values in DFS (pre-order) order using the fixed method.

        Time Complexity:  O(n) — every node visited exactly once.
        Space Complexity: O(h) — call stack depth equals tree height h.
        """
        return root.depth_first_search()
