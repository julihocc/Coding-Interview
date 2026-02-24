"""TEMPLATE: Company Hierarchy DFS Traversal

Reference: See ../README.md for full problem description
"""


class Node:
    """A node in a company hierarchy tree."""

    def __init__(self, value: str):
        self.value = value
        self.children: list["Node"] = []


class Solution:
    def dfs(self, root: Node) -> list[str]:
        """Return department names in DFS (pre-order) traversal order.

        Args:
            root: The root node of the company hierarchy tree.

        Returns:
            A list of department/team name strings in the order first visited by DFS.
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
        result = instance.dfs(case.root)
        return result == case.expected

    test_solution(Solution, TEST_CASES, run_case_logic)
