class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Optimized Approach for Identifying K-th Smallest Element

    Uses node counting to determine whether the target lies in the left
    subtree, the right subtree, or is the current root node itself.

    Time Complexity: O(h + k) - Bounded by recursion depth and k iterations
    Space Complexity: O(h) - Maximal depth of recursion stack
    """

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        left_nodes = self._countNodes(root.left) if root else 0

        if k == left_nodes + 1:
            return root.val
        elif k <= left_nodes:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - 1 - left_nodes)

    def _countNodes(self, node: TreeNode) -> int:
        if not node:
            return 0
        return 1 + self._countNodes(node.left) + self._countNodes(node.right)
