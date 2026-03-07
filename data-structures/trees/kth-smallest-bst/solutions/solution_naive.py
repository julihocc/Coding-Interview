class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Naive Approach for Identifying K-th Smallest Element

    Traverses the tree, stores elements in an array, sorts them, and retrieves the k-th.

    Time Complexity: O(n log n) - Sort operation over all BST elements
    Space Complexity: O(n) - The array holds all tree entries in memory
    """

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        elements = []
        self._traverse(root, elements)
        elements.sort()

        # k is 1-indexed
        return elements[k - 1]

    def _traverse(self, node: TreeNode, elements: list):
        if not node:
            return

        self._traverse(node.left, elements)
        elements.append(node.val)
        self._traverse(node.right, elements)
