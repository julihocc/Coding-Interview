class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Optimized Approach for Checking Binary Search Tree Balance

    Time Complexity: O(n) - Each node is visited exactly once
    Space Complexity: O(n) - Maximum depth of the recursion stack (O(log n) if balanced)
    """

    def is_balanced(self, root: TreeNode) -> bool:
        height, is_bal = self._check_balance(root)
        return is_bal

    def _check_balance(self, node: TreeNode) -> tuple[int, bool]:
        if node is None:
            return 0, True

        left_height, left_balanced = self._check_balance(node.left)
        if not left_balanced:
            return -1, False

        right_height, right_balanced = self._check_balance(node.right)
        if not right_balanced:
            return -1, False

        height = max(left_height, right_height) + 1
        is_balanced_condition = abs(left_height - right_height) <= 1
        return height, is_balanced_condition
