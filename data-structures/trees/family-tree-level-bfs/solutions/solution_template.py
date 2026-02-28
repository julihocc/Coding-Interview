"""TEMPLATE: Family Tree Level BFS

Reference: See ../README.md for full problem description
"""

from collections import deque
from typing import Dict, List


class Solution:
    def bfs_level(self, graph: Dict[str, List[str]], root: str = "1") -> Dict[str, int]:
        """Perform Breadth-first Search on a family tree graph to find levels.

        Args:
            graph: A dictionary mapping family member IDs to lists of their children.
            root: The starting monarch ID.

        Returns:
            A dictionary mapping each visited family member ID to their level.
        """
        visited = []
        queue = deque()
        queue.append(root)

        # level = ___ # TODO: initialize levels dictionary

        while queue:
            vertex = queue.popleft()
            visited.append(vertex)

            # level_of_vertex = ___ # TODO: set the current level of vertex

            for child in graph.get(vertex, []):
                if child not in visited and child not in queue:
                    queue.append(child)
                    # level[child] = ___ # TODO: set the level of the child

        return {}  # Replace with returning the level dictionary


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
        graph, root = case.input
        result = instance.bfs_level(graph, root)
        return result == case.expected

    test_solution(Solution, TEST_CASES, run_case_logic)
