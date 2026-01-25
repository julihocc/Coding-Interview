"""TEMPLATE: Function-based solution for Search Insert Position

Reference: See ../README.md for full problem description
"""

class Solution:
    def search_insert(self, nums: list[int], target: int) -> int:
        """Find the index where target is found or where it would be if inserted in order.

        Args:
            nums: A list of integers sorted in non-decreasing order.
            target: The integer value to search for/insert.

        Returns:
            The index of the target or the insertion index.
        """
        # TODO: Implement your solution here
        raise NotImplementedError("Solution not implemented yet")
        return 0

if __name__ == "__main__":
    import sys
    import os

    # Add the project root to sys.path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    problem_dir = os.path.dirname(current_dir)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(problem_dir)))
    
    sys.path.append(project_root)
    sys.path.append(problem_dir)

    from utils.judge_utils import test_solution
    from tests.cases import TEST_CASES

    def run_case_logic(SolutionClass, case):
        instance = SolutionClass()
        result = instance.search_insert(list(case.nums), case.target)
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
