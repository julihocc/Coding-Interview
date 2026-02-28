"""TEMPLATE: Breadth-first Search on Trees

Reference: See ../README.md for full problem description
"""

from collections import deque
from typing import Dict, List


class Solution:
    def bfs(self, tree: Dict[str, List[str]], root: str) -> List[str]:
        """Perform Breadth-first Search on a tree.

        Args:
            tree: A dictionary mapping node names to lists of child node names.
            root: The starting root node name.

        Returns:
            A list of node names in the order they were visited.
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
        tree, root = case.input
        result = instance.bfs(tree, root)
        return result == case.expected

    test_solution(Solution, TEST_CASES, run_case_logic)
