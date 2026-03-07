class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_height_diff(self, root: TreeNode) -> int:
        """
        Finds the maximum difference between heights of left and right subtrees
        for any node in the given BST.

        Args:
            root: TreeNode representing the root of the tree

        Returns:
            int: The maximum height difference found

        Time Complexity: O(n) optimally, where n is the number of nodes
        Space Complexity: O(h) optimally, where h is the height of the tree
        """
        # TODO: Implement an efficient traversal to track the maximum difference
        raise NotImplementedError("This method needs to be implemented by you.")
