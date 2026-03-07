class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_balanced(self, root: TreeNode) -> bool:
        """
        Checks if a Binary Search Tree is balanced.
        A tree is balanced if for each vertex, the size of the left subtree
        differs from the size of the right subtree by at most 1.

        Args:
            root: TreeNode representing the root of the tree

        Returns:
            bool: True if the tree is balanced, False otherwise

        Time Complexity: O(n) ideally, where n is the number of nodes
        Space Complexity: O(h) ideally, where h is the height of the tree
        """
        # TODO: Implement this to check if the tree is balanced
        raise NotImplementedError("This method needs to be implemented by you.")
