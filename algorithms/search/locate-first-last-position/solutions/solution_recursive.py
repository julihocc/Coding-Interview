from typing import List


class Solution:
    def search_range(self, nums: List[int], target: int) -> List[int]:
        """
        Finds the first and last position of a target element in a sorted array using recursive binary search.
        """
        n = len(nums)
        if n == 0:
            return [-1, -1]
            
        first = self._find_first(nums, target, 0, n - 1)
        if first == -1:
            return [-1, -1]
            
        last = self._find_last(nums, target, 0, n - 1)
        return [first, last]
        
    def _find_first(self, nums, target, low, high):
        if low > high:
            return -1
            
        mid = (low + high) // 2
        
        if nums[mid] == target:
            left_res = self._find_first(nums, target, low, mid - 1)
            if left_res != -1:
                return left_res
            return mid
        elif nums[mid] < target:
            return self._find_first(nums, target, mid + 1, high)
        else:
            return self._find_first(nums, target, low, mid - 1)
            
    def _find_last(self, nums, target, low, high):
        if low > high:
            return -1
            
        mid = (low + high) // 2
        
        if nums[mid] == target:
            right_res = self._find_last(nums, target, mid + 1, high)
            if right_res != -1:
                return right_res
            return mid
        elif nums[mid] < target:
            return self._find_last(nums, target, mid + 1, high)
        else:
            return self._find_last(nums, target, low, mid - 1)

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
        result = instance.search_range(list(case.nums), case.target)
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
