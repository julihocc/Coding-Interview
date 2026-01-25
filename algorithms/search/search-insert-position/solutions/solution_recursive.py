from typing import List


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        """
        Finds the insert position (lower bound) of a target element in a sorted array using recursive binary search.
        If duplicates exist, returns the index of the first occurrence.
        """
        return self._search_recursive(nums, target, 0, len(nums) - 1)

    def _search_recursive(self, nums: List[int], target: int, low: int, high: int) -> int:
        if low > high:
            return low
        
        mid = (low + high) // 2
        
        if nums[mid] >= target:
            # Even if we found it, we must check left to guarantee finding the first occurrence
            # effectively reducing the search space to [low, mid-1] and eventually returning 'low' (which will be this mid or smaller)
            # Standard logic: if matches, treat as if it's "greater or equal" and push search left, 
            # the answer will be in the 'low' variable when high < low. 
            # In recursion, we just return the result of the left subproblem.
            # But wait, we need to distinguish.
            # bisect_left logic:
            # if x < a[mid]: high = mid
            # else: low = mid + 1
            # Here indices are inclusive.
            return self._search_recursive(nums, target, low, mid - 1)
        else:
            return self._search_recursive(nums, target, mid + 1, high)

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
