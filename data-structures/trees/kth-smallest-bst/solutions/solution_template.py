class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Finds the k-th smallest element in a Binary Search Tree.

        Args:
            root: TreeNode representing the root of the tree
            k: 1-indexed target position for the k-th smallest element

        Returns:
            int: The value of the k-th smallest node

        Time Complexity: O(h + k) optimally
        Space Complexity: O(h) ideally
        """
        # TODO: Implement this to find the k-th smallest element
        raise NotImplementedError("This method needs to be implemented by you.")
