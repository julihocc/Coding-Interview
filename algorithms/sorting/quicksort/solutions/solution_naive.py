from typing import List


class Solution:
    """Use built-in sort to return a sorted copy."""

    def __init__(self, nums: List[int]):
        self.nums = nums

    def quicksort(self) -> List[int]:
        return sorted(self.nums)

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
        instance = SolutionClass(list(case.nums))
        result = instance.quicksort()
        return result == sorted(case.nums)
    
    test_solution(Solution, TEST_CASES, run_case_logic)
