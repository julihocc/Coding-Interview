"""TEMPLATE: Browser History Tree — Pre-Order Traversal

Reference: See ../README.md for full problem description
"""
from typing import Optional


class TreeNode:
    """A node in the browser history tree."""
    def __init__(self, value: str):
        self.value = value
        self.children: list["TreeNode"] = []

    def add_child(self, child_node: "TreeNode") -> None:
        self.children.append(child_node)

    def remove_child(self, child_node: "TreeNode") -> None:
        self.children = [c for c in self.children if c is not child_node]


class Solution:
    def pre_order(self, root: Optional[TreeNode]) -> list[str]:
        """Return all visited URLs in pre-order (DFS) traversal.

        Visit the current page first, then recursively visit each child
        page in order (left to right).

        Args:
            root: The root node of the browser history tree, or None.

        Returns:
            A list of URL strings in pre-order (root → children) order.
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
        result = instance.pre_order(case.root)
        return result == case.expected

    test_solution(Solution, TEST_CASES, run_case_logic)
