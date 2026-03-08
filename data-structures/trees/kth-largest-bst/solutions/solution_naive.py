class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Naive Approach for K-th Largest Element

    Traverses the tree to collect all elements in a list, then returns
    the k-th element from the end of the sorted collection.

    Time Complexity: O(n) - We visit every node to build the list
    Space Complexity: O(n) - We store all nodes in the list
    """

    def kth_largest(self, root: TreeNode, k: int) -> int:
        self.elements = []
        self._in_order(root)
        return self.elements[-k]

    def _in_order(self, node: TreeNode):
        if not node:
            return

        self._in_order(node.left)
        self.elements.append(node.val)
        self._in_order(node.right)
