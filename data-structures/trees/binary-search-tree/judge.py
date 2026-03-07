import sys
import os
import time
from typing import List, Type

# Add the repository root to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Add the problem directory to the path so we can import from tests and solutions
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.judge_utils import load_classes, run_tests
from tests.cases import TestCase, cases
from solutions.solution_optimized import Node


def get_inorder(root: Node) -> List[int]:
    """Helper to retrieve the BST in-order traversal to verify its state."""
    if not root:
        return []
    return get_inorder(root.left) + [root.val] + get_inorder(root.right)


def run_test_case(solution_class: Type, case: TestCase) -> bool:
    """
    Executes a single test case using the provided solution class.

    Args:
        solution_class: The class to instantiate and test
        case: The TestCase containing input and expected output

    Returns:
        bool: True if test passes, False otherwise
    """
    try:
        # 1. Instantiate the class
        bst = solution_class()

        # 2. Insert values in the sequence provided
        for val in case.inserts:
            bst.insert(val)

        # 3. Search values to see if they're present
        search_results = []
        for val in case.searches:
            node = bst.search(val)
            search_results.append(node is not None)

        if search_results != case.expected_searches:
            print(f"    Expected searches: {case.expected_searches}")
            print(f"    Got searches     : {search_results}")
            return False

        # 4. Perform deletions
        for val in case.deletes:
            bst.delete(val)

        # 5. Extract tree content via in-order traversal and match
        inorder_after = get_inorder(bst.root) if getattr(bst, "root", None) else []

        if inorder_after != case.expected_inorder_after:
            print(f"    Expected inorder: {case.expected_inorder_after}")
            print(f"    Got inorder     : {inorder_after}")
            return False

        return True

    except Exception as e:
        print(f"    Exception raised: {e}")
        return False


if __name__ == "__main__":
    # Get the directory of this problem
    problem_dir = os.path.dirname(os.path.abspath(__file__))

    # Load all solutions
    reference_solutions = load_classes(
        os.path.join(problem_dir, "solutions"), "BinarySearchTree", subfolder=None
    )
    contributed_solutions = load_classes(
        os.path.join(problem_dir, "solutions", "contributed"),
        "BinarySearchTree",
        subfolder=None,
    )

    # Run tests using the shared utility
    print("=== REFERENCE SOLUTIONS ===")
    run_tests(reference_solutions, cases, run_test_case)

    print("\n=== CONTRIBUTED SOLUTIONS ===")
    run_tests(contributed_solutions, cases, run_test_case)
