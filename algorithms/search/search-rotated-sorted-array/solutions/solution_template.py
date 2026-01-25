"""TEMPLATE: Class-based solution for Search Rotated Sorted Array

Reference: See ../README.md for full problem description
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Search for a target value in a rotated sorted array.

        Args:
            nums: A list of integers sorted in ascending order (with distinct values)
                  that is rotated at some pivot unknown to you beforehand.
            target: The integer value to search for.

        Returns:
            The index of target if it is in nums, or -1 if it is not in nums.
        """
        # TODO: Implement your solution here
        raise NotImplementedError("Solution not implemented yet")
        return -1

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
        result = instance.search(list(case.nums), case.target)
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
