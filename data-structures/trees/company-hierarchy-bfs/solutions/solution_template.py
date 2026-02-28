"""TEMPLATE: Company Hierarchy BFS

Reference: See ../README.md for full problem description
"""

from collections import deque
from typing import Dict, List


class Solution:
    def bfs(self, graph: Dict[str, List[str]], root: str = "1") -> List[str]:
        """Perform Breadth-first Search on a company hierarchy graph.

        The implementation below contains a bug. Your task is to fix it.

        Args:
            graph: A dictionary mapping employee IDs to lists of their direct reports.
            root: The starting CEO ID.

        Returns:
            A list of employee IDs in the order they were visited.
        """
        visited = []  # List to keep track of visited nodes
        queue = deque()
        queue.append(root)  # Start with the root node

        while queue:  # While there are nodes to visit.
            vertex = queue.popleft()  # Visit the first node in the queue

            # Now add all unvisited children to the queue
            for child in graph.get(vertex, []):
                if child not in visited:
                    visited.append(child)

        return visited


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
        result = instance.bfs(graph, root)
        return result == case.expected

    test_solution(Solution, TEST_CASES, run_case_logic)
