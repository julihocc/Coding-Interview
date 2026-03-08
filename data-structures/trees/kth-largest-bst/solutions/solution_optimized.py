class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Optimized Approach for K-th Largest Element

    Uses reverse in-order traversal (Right -> Root -> Left) to visit elements
    in strictly descending order. Stops memory accumulation early once `k`
    elements have been counted.

    Time Complexity: O(h + k) - We traverse down to rightmost element (h steps), then process k nodes. Max $O(N)$
    Space Complexity: O(h) - Maximal depth of recursion stack (O(log n) if balanced).
    """

    def kth_largest(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.result = 0
        self._reverse_in_order(root, k)
        return self.result

    def _reverse_in_order(self, node: TreeNode, k: int):
        if not node or self.count >= k:
            return

        # 1. Right subtree contains larger elements
        self._reverse_in_order(node.right, k)

        # 2. Process current node
        self.count += 1
        if self.count == k:
            self.result = node.val
            return

        # 3. Left subtree contains smaller elements
        self._reverse_in_order(node.left, k)
