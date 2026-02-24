"""TEMPLATE: Depth-First Search (DFS) on Trees

Reference: See ../README.md for full problem description
"""


class Solution:
    def dfs(self, tree: dict, root: str) -> list[str]:
        """Return all nodes reachable from root in DFS order.

        Args:
            tree: Adjacency dictionary representing the tree.
                  Connections are bidirectional (parent lists child AND child lists parent).
            root: The starting node label.

        Returns:
            A list of node labels in the order they are first visited by DFS.
        """
        # TODO: Implement your solution here
        raise NotImplementedError("Solution not implemented yet")

    def find_path(self, tree: dict, start: str, end: str) -> list[str] | None:
        """Find a path from start to end using DFS.

        Args:
            tree: Adjacency dictionary representing the tree.
            start: The starting node label.
            end: The target node label.

        Returns:
            A list of node labels forming the path from start to end,
            or None if no path exists.
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
        if case.mode == "traversal":
            result = instance.dfs(case.tree, case.start)
        else:
            result = instance.find_path(case.tree, case.start, case.end)
        return result == case.expected

    test_solution(Solution, TEST_CASES, run_case_logic)
