from typing import List


class Solution:
    """Binary search to locate target index in a sorted array."""

    def __init__(self, nums: List[int]):
        self.nums = nums

    def target_index_search(self, target: int) -> int:
        left, right = 0, len(self.nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.nums[mid] == target:
                return mid
            if self.nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

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
        instance = SolutionClass(list(case.nums))
        result = instance.target_index_search(case.target)
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
