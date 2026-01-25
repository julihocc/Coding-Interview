from typing import List


class Solution:
    def search_range(self, nums: List[float], target: float) -> List[int]:
        """
        Finds the first and last position of a target float in a sorted array using linear scan.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        first, last = -1, -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        
        return [first, last]

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
