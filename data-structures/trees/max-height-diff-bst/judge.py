import sys
import os

# Add parent directory to path to allow importing solutions and tests
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    )
)

from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Helper to build trees from list representation (level order)"""
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


def run_case_logic(SolutionClass, case) -> bool:
    """
    Executes a single test case using the provided SolutionClass.
    Returns True if the test passes, False otherwise.
    """
    try:
        # The judge framework initializes the class and calls the method
        instance = SolutionClass()

        # Build the tree using the helper function
        root = None
        if len(case.tree) > 0:
            root = build_tree(case.tree)

        result = instance.max_height_diff(root)

        if result == case.expected:
            return True
        else:
            print(f"    Expected: {case.expected}")
            print(f"    Got:      {result}")
            return False

    except Exception as e:
        print(f"    Error executing case: {e}")
        return False


if __name__ == "__main__":
    sys.exit(run_judge_from_file(__file__, TEST_CASES, run_case_logic))
