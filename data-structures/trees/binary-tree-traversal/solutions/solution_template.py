"""TEMPLATE: Binary Tree In-Order Traversal

Reference: See ../README.md for full problem description
"""
from typing import Optional


class Node:
    """A node in a binary tree."""
    def __init__(self, value: int):
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class Solution:
    def in_order(self, root: Optional[Node]) -> list[int]:
        """Return the in-order traversal of the binary tree as a list of values.

        Args:
            root: The root node of the binary tree, or None for an empty tree.

        Returns:
            A list of integer values in left → root → right order.
        """
        # TODO: Implement your solution here
        raise NotImplementedError("Solution not implemented yet")


if __name__ == "__main__":
    import sys
    import os

    current_dir = os.path.dirname(os.path.abspath(__file__))
    problem_dir = os.path.dirname(current_dir)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(problem_dir)))

    sys.path.append(project_root)
    sys.path.append(problem_dir)

    from utils.judge_utils import test_solution
    from tests.cases import TEST_CASES

    def run_case_logic(SolutionClass, case):
        instance = SolutionClass()
        result = instance.in_order(case.root)
        return result == case.expected

    test_solution(Solution, TEST_CASES, run_case_logic)
