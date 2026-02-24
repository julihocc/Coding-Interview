"""TEMPLATE: Planet Continents DFS Traversal

Reference: See ../README.md for full problem description
"""

from tests.cases import Node


class Solution:
    def extend_and_traverse(self, root: Node) -> list[str]:
        """Extend the tree with new countries and return DFS traversal order.

        Steps:
          1. Locate the Africa node (root.children[0]) and add two countries.
          2. Locate the Asia node (root.children[1]) and add two countries.
          3. Call root.depth_first_search() and return the traversal list.

        Args:
            root: The root 'Earth' node of the planet hierarchy tree.

        Returns:
            A list of node values in DFS visit order.
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
        result = instance.extend_and_traverse(case.root)
        return result == case.expected

    test_solution(Solution, TEST_CASES, run_case_logic)
