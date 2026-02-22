"""TEMPLATE: Company Hierarchy Tree — Restructure and Traverse

Reference: See ../README.md for full problem description
"""
from typing import Optional


class TreeNode:
    """A node in the company hierarchy tree."""
    def __init__(self, value: str):
        self.value = value
        self.children: list["TreeNode"] = []

    def add_child(self, child_node: "TreeNode") -> None:
        self.children.append(child_node)

    def remove_child(self, child_node: "TreeNode") -> None:
        self.children = [c for c in self.children if c is not child_node]


class Solution:
    def restructure_and_traverse(self, root: Optional[TreeNode]) -> list[str]:
        """Restructure the company tree and return its pre-order traversal.

        Steps to implement:
          1. Find the "VP Engineering" node using DFS search.
          2. Find the "Engineer" node (currently a child of VP Engineering).
          3. Create a new TreeNode("Senior Engineer").
          4. Create a new TreeNode("Product Manager").
          5. Remove "Engineer" from "VP Engineering".
          6. Add "Engineer" as a child of "Senior Engineer".
          7. Add "Senior Engineer" as a child of "VP Engineering".
          8. Add "Product Manager" as a child of "VP Engineering".
          9. Return the pre-order traversal of the updated tree.

        Args:
            root: The root of the initial company hierarchy tree.

        Returns:
            A list of position strings in pre-order (root → children) order.
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
        result = instance.restructure_and_traverse(case.root)
        return result == case.expected

    test_solution(Solution, TEST_CASES, run_case_logic)
