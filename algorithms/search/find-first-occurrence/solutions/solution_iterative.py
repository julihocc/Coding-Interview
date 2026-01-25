from typing import List


class Solution:
    """Binary search with left refinement to find the first occurrence."""

    def __init__(self, nums: List[int]):
        self.nums = nums

    def find_first_occurrence(self, target: int) -> int:
        low, high = 0, len(self.nums) - 1
        result = -1

        while low <= high:
            mid = (low + high) // 2
            if self.nums[mid] == target:
                result = mid
                high = mid - 1
            elif self.nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return result

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
        result = instance.find_first_occurrence(case.target)
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
