class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Optimized Approach for Maximum Subtree Height Difference

    Calculates height bottom-up via post-order traversal, simultaneously tracking
    the maximum difference without recalculating heights unnecessarily.

    Time Complexity: O(n) - Each node is visited exactly once
    Space Complexity: O(h) - Maximum depth of the recursion stack (O(log n) if balanced)
    """

    def max_height_diff(self, root: TreeNode) -> int:
        self.max_diff = 0
        self._get_height_and_diff(root)
        return self.max_diff

    def _get_height_and_diff(self, node: TreeNode) -> int:
        if not node:
            return 0

        left_height = self._get_height_and_diff(node.left)
        right_height = self._get_height_and_diff(node.right)

        current_diff = abs(left_height - right_height)
        if current_diff > self.max_diff:
            self.max_diff = current_diff

        return max(left_height, right_height) + 1
