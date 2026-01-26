from typing import List

class Solution:
    def insert_position(self, nums: List[int], target: int) -> int:
        """
        Finds the insert position using recursive binary search.
        Time Complexity: O(log n)
        Space Complexity: O(log n) due to recursion stack
        """
        return self._search(nums, target, 0, len(nums))

    def _search(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left >= right:
            return left
            
        mid = (left + right) // 2
        
        if nums[mid] < target:
            return self._search(nums, target, mid + 1, right)
        else:
            return self._search(nums, target, left, mid)

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
        result = instance.insert_position(list(case.nums), case.target)
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
