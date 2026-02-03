"""Naive O(n²) solution for counting anti-inversion pairs.

Time complexity: O(n²) - nested loops to check all pairs
Space complexity: O(1) - only counter variable needed
"""

from typing import List


class Solution:
    """Brute force approach to count anti-inversion pairs."""

    def __init__(self, arr: List[int]):
        """Initialize with the array to analyze.
        
        Args:
            arr: List of integers to count anti-inversions in
        """
        self.arr = arr

    def count_anti_inversions(self) -> int:
        """Count pairs (i, j) where i < j and arr[i] < arr[j].
        
        Uses nested loops to check all possible pairs.
        
        Returns:
            Total count of anti-inversion pairs
        """
        count = 0
        n = len(self.arr)
        
        for i in range(n):
            for j in range(i + 1, n):
                if self.arr[i] < self.arr[j]:
                    count += 1
        
        return count


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
        instance = SolutionClass(list(case.arr))
        result = instance.count_anti_inversions()
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
