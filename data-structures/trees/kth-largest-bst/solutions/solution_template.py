class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kth_largest(self, root: TreeNode, k: int) -> int:
        """
        Finds the k-th largest element in a Binary Search Tree.

        Args:
            root: TreeNode representing the root of the tree
            k: The 1-based index of the largest element to find

        Returns:
            int: The value of the k-th largest element

        Time Complexity: O(h + k) optimally
        Space Complexity: O(h) optimally
        """
        # TODO: Implement a reverse in-order traversal
        raise NotImplementedError("This method needs to be implemented by you.")
