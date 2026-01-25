from typing import List


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        """
        Finds the insert position of a target element in a sorted array using recursive binary search.
        """
        return self._search_recursive(nums, target, 0, len(nums) - 1)

    def _search_recursive(self, nums: List[int], target: int, low: int, high: int) -> int:
        if low > high:
            return low
        
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self._search_recursive(nums, target, mid + 1, high)
        else:
            return self._search_recursive(nums, target, low, mid - 1)

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
