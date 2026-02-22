"""TEMPLATE: Non-Binary Tree Level-Order Traversal

Reference: See ../README.md for full problem description
"""
from typing import Optional


class Node:
    """A node in a non-binary (multi-way) tree."""
    def __init__(self, value: int):
        self.value = value
        self.children: list["Node"] = []


class Solution:
    def level_order(self, root: Optional[Node]) -> list[int]:
        """Return the level-order (BFS) traversal of the non-binary tree.

        Args:
            root: The root node of the tree, or None for an empty tree.

        Returns:
            A list of integer values visited level by level, left to right.
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
        result = instance.level_order(case.root)
        return result == case.expected

    test_solution(Solution, TEST_CASES, run_case_logic)
