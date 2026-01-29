"""Naive solution using Python's built-in sort.

This solution demonstrates the simplest approach to sorting by leveraging
Python's highly optimized Timsort algorithm.
"""

from typing import List


class Solution:
    """Naive approach using built-in sorted() function."""

    def __init__(self, nums: List[int]):
        """Initialize with the array to sort.
        
        Args:
            nums: An unsorted list of integers.
        """
        self.nums = nums

    def merge_sort(self) -> List[int]:
        """Sort using Python's built-in sorted() function.
        
        Returns:
            A new sorted list containing all elements from self.nums.
        """
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
        result = instance.merge_sort()
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
