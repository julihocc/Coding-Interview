class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Naive Approach for Maximum Subtree Height Difference

    Traverses the tree top-down and for each node, calculates the height of both
    its subtrees to find their difference, maintaining a running maximum.

    Time Complexity: O(n^2) - As for every node, we calculate the height of its subtrees
    Space Complexity: O(n) - Maximum depth of the recursion stack
    """

    def max_height_diff(self, root: TreeNode) -> int:
        self.max_diff = 0
        self._traverse(root)
        return self.max_diff

    def _traverse(self, node: TreeNode):
        if not node:
            return

        left_h = self._get_height(node.left)
        right_h = self._get_height(node.right)

        self.max_diff = max(self.max_diff, abs(left_h - right_h))

        self._traverse(node.left)
        self._traverse(node.right)

    def _get_height(self, node: TreeNode) -> int:
        if not node:
            return 0
        return max(self._get_height(node.left), self._get_height(node.right)) + 1
