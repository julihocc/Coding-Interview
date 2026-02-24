"""TEMPLATE: Galactic Hierarchy DFS — Debug the Bug

Reference: See ../README.md for full problem description

The original buggy code called self.depth_first_search() inside the child
loop instead of child.depth_first_search(). This causes infinite recursion.

Your task: Fix the depth_first_search method and return the traversal as a list.
"""

from tests.cases import TreeNode


class Solution:
    def dfs(self, root: TreeNode) -> list[str]:
        """Return node values in DFS (pre-order) order using the fixed method.

        Args:
            root: The root TreeNode of the galactic hierarchy.

        Returns:
            A list of node values in the order they are visited by DFS.
        """
        # TODO: Implement your solution here
        # Hint: call root.depth_first_search() — but make sure the method
        #       calls child.depth_first_search(), not self.depth_first_search()!
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
