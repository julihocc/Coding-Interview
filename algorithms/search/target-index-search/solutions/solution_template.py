"""TEMPLATE: Class-based solution for Target Index Search

Implement a class whose name reflects the strategy (e.g., BinarySearchTargetIndexFinder).
Judges instantiate your class with nums in __init__ and call the method.

Reference: See ../README.md for full problem description
"""

from typing import List


class YourTargetIndexFinder:
    """Rename and implement this class to match your approach.
    
    Example strategies: LinearTargetIndexFinder, BinarySearchTargetIndexFinder
    """

    def __init__(self, nums: List[int]):
        """Initialize with the sorted array to search in.
        
        Args:
            nums: A sorted list of integers to search within.
        """
        self.nums = nums

    def target_index_search(self, target: int) -> int:
        """Find the index of target in a sorted array.
        
        Expected behavior:
        - Return the index where self.nums[index] == target
        - Return -1 if target is not found
        - For sorted arrays, binary search is more efficient than linear scan
        
        Args:
            target: The value to search for.
            
        Returns:
            The index of the target, or -1 if not found.
        """
        # TODO: Implement search strategy
        # Consider: Linear scan vs. Binary search
        # For binary search, adjust left/right pointers based on comparison
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
        result = instance.target_index_search(case.target)
        return result == case.expected
    
    test_solution(YourTargetIndexFinder, TEST_CASES, run_case_logic)
