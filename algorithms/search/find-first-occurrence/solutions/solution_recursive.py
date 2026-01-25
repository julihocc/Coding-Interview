from typing import List


class Solution:
    """Recursive binary search with left refinement to find the first occurrence."""

    def __init__(self, nums: List[int]):
        self.nums = nums

    def find_first_occurrence(self, target: int) -> int:
        return self._helper(0, len(self.nums) - 1, target)

    def _helper(self, low: int, high: int, target: int) -> int:
        if low > high:
            return -1
        
        mid = (low + high) // 2
        
        if self.nums[mid] == target:
            # We found the target, but we want the FIRST occurrence.
            # Try searching to the left to see if there's an earlier one.
            left_result = self._helper(low, mid - 1, target)
            if left_result != -1:
                return left_result
            else:
                return mid
        elif self.nums[mid] < target:
            return self._helper(mid + 1, high, target)
        else:
            return self._helper(low, mid - 1, target)

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
