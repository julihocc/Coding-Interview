"""TEMPLATE: Class-based solution for Find First Occurrence

Implement a class whose name conveys the strategy (e.g., BinarySearchFinder).
Judges instantiate your class with array data in __init__ and call the method.

Reference: See ../README.md for full problem description
"""

from typing import List


class Solution:
    """Rename and implement this class to match your approach.
    
    Example strategies: LinearScanFinder, BinarySearchFinder
    """

    def __init__(self, nums: List[int]):
        """Initialize with the sorted array to search in.
        
        Args:
            nums: A sorted list of integers to search within.
        """
        self.nums = nums

    def find_first_occurrence(self, target: int) -> int:
        """Find the index of the first occurrence of target in self.nums.
        
        Expected behavior:
        - Return the smallest index i where self.nums[i] == target
        - Return -1 if target is not found
        - For a sorted array with duplicates, return the leftmost occurrence
        
        Args:
            target: The value to search for.
            
        Returns:
            The index of the first occurrence, or -1 if not found.
        """
        # TODO: Implement search strategy
        # Consider: Linear scan vs. Binary search with left refinement
        raise NotImplementedError("Search strategy not implemented yet")

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
