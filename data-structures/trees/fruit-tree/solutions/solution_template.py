"""TEMPLATE: Fruit Tree — Insert Node and Pre-Order Traversal

Reference: See ../README.md for full problem description
"""
from typing import Optional


class TreeNode:
    """A node in the fruit tree."""
    def __init__(self, value: str):
        self.value = value
        self.children: list["TreeNode"] = []

    def add_child(self, child_node: "TreeNode") -> None:
        self.children.append(child_node)

    def remove_child(self, child_node: "TreeNode") -> None:
        self.children = [c for c in self.children if c is not child_node]


class Solution:
    def insert_and_traverse(self, root: Optional[TreeNode]) -> list[str]:
        """Insert Plum under Pear, then return pre-order traversal.

        Steps to implement:
          1. Find the "Pear" node in the tree using DFS search.
          2. Call pear_node.add_child(TreeNode("Plum")) to insert it.
          3. Return the pre-order traversal of the updated tree
             (i.e., implement print_tree but collect values into a list).

        Args:
            root: The root of the initial fruit tree.

        Returns:
            A list of fruit names in pre-order (root → children) order.
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
        result = instance.insert_and_traverse(case.root)
        return result == case.expected

    test_solution(Solution, TEST_CASES, run_case_logic)
