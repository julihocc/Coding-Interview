"""TEMPLATE: Department Tree DFS — Implement the Missing Logic

Reference: See ../README.md for full problem description

The traverse() method already handles visiting the current node.
Your task: add the recursive loop that visits each subdepartment.
"""

from tests.cases import DepartmentTree


class Solution:
    def dfs(self, root: DepartmentTree) -> list[str]:
        """Return department names in DFS (pre-order) order.

        Args:
            root: The root DepartmentTree node (e.g. 'CEO').

        Returns:
            A list of department name strings in DFS visit order.
        """
        # TODO: Implement your solution here
        # Hint: call root.traverse() after completing the traverse() method.
        # The missing logic in traverse() should:
        #   1. Iterate over self.subdepartments
        #   2. Check if subdept.name is not in visited
        #   3. Recursively call subdept.traverse(visited, result)
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
