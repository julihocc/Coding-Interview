from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Search in a rotated sorted array (descending) using recursive binary search.
        """
        return self._search_recursive(nums, target, 0, len(nums) - 1)

    def _search_recursive(self, nums, target, low, high):
        if low > high:
            return -1
        
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
            
        # Left Side is Sorted (Descending)
        if nums[low] >= nums[mid]:
            if nums[low] >= target > nums[mid]:
                return self._search_recursive(nums, target, low, mid - 1)
            else:
                return self._search_recursive(nums, target, mid + 1, high)
        # Right Side is Sorted (Descending)
        else:
            if nums[mid] > target >= nums[high]:
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
        result = instance.search(list(case.nums), case.target)
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
