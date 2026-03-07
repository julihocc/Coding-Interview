import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from solutions.solution_optimized import TreeNode, is_balanced, kthSmallest
except ImportError:
    pass  # Judge will inject these


# Helper to build trees from list representation (level order)
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        current = queue.pop(0)

        if i < len(values) and values[i] is None:
            pass  # skip None
        elif i < len(values):
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is None:
            pass  # skip None
        elif i < len(values):
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root


# --- Problem 1: is_balanced Test Cases ---
BALANCE_TEST_CASES = [
    {
        "name": "Balanced tree 1",
        "tree": [3, 9, 20, None, None, 15, 7],
        "expected": True,
    },
    {
        "name": "Unbalanced tree 1",
        "tree": [1, 2, 2, 3, 3, None, None, 4, 4],
        "expected": False,
    },
    {"name": "Empty tree", "tree": [], "expected": True},
    {"name": "Single node", "tree": [1], "expected": True},
    {
        "name": "Left linear unbalanced",
        "tree": [1, 2, None, 3, None, 4],
        "expected": False,
    },
]

# --- Problem 2: kthSmallest Test Cases ---
KTH_TEST_CASES = [
    {"name": "k=1 in small tree", "tree": [3, 1, 4, None, 2], "k": 1, "expected": 1},
    {
        "name": "k=3 in medium tree",
        "tree": [5, 3, 6, 2, 4, None, None, 1],
        "k": 3,
        "expected": 3,
    },
    {
        "name": "k=1 in a linear-left tree",
        "tree": [10, 8, None, 6, None, 4],
        "k": 1,
        "expected": 4,
    },
    {
        "name": "k=4 in a linear-right tree",
        "tree": [1, None, 2, None, 3, None, 4],
        "k": 4,
        "expected": 4,
    },
    {"name": "k is the root element", "tree": [5, 2, 8], "k": 2, "expected": 5},
]
