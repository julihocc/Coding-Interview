class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Naive Approach for Checking Binary Search Tree Balance

    Time Complexity: O(n^2) - As for every node, we calculate the height of its subtrees
    Space Complexity: O(n) - Maximum depth of the recursion stack
    """

    def is_balanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        left_height = self._get_height(root.left)
        right_height = self._get_height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.is_balanced(root.left) and self.is_balanced(root.right)

    def _get_height(self, node: TreeNode) -> int:
        if not node:
            return 0
        return max(self._get_height(node.left), self._get_height(node.right)) + 1
