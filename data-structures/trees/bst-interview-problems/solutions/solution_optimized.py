class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: TreeNode) -> bool:
    # returns (height, is_balanced)
    def check_balance(node) -> tuple[int, bool]:
        if node is None:
            return 0, True

        left_height, left_balanced = check_balance(node.left)
        if not left_balanced:
            return -1, False

        right_height, right_balanced = check_balance(node.right)
        if not right_balanced:
            return -1, False

        height = max(left_height, right_height) + 1
        is_balanced = abs(left_height - right_height) <= 1
        return height, is_balanced

    height, balanced = check_balance(root)
    return balanced


def kthSmallest(root: TreeNode, k: int) -> int:
    # The number of nodes in the left subtree of the root
    left_nodes = countNodes(root.left) if root else 0

    # If k is equal to the number of nodes in the left subtree plus 1,
    # That means we must return the root's value as we've reached the k-th smallest
    if k == left_nodes + 1:
        return root.val
    # If there are more than k nodes in the left subtree,
    # The k-th smallest must be in the left subtree.
    elif k <= left_nodes:
        return kthSmallest(root.left, k)
    # If there are less than k nodes in the left subtree,
    # The k-th smallest must be in the right subtree.
    else:
        return kthSmallest(root.right, k - 1 - left_nodes)


def countNodes(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)
