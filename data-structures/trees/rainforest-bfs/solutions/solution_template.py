"""TEMPLATE: Rainforest BFS

Reference: See ../README.md for full problem description
"""

from collections import deque
from typing import Dict, List


class Solution:
    def bfs(
        self, forest: Dict[str, List[str]], root: str = "Amazon_Rainforest"
    ) -> List[str]:
        """Perform Breadth-first Search on a forest.

        Args:
            forest: A dictionary mapping forest names to lists of neighboring forest names.
            root: The starting forest name.

        Returns:
            A list of forest names in the order they were visited.
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
        forest, root = case.input
        result = instance.bfs(forest, root)
        return result == case.expected

    test_solution(Solution, TEST_CASES, run_case_logic)
