"""Naive solution using Python's built-in sort with key function.

This solution demonstrates the simplest approach by using sorted() with
a custom key function that extracts the first 3 characters for comparison.
"""

from typing import List


class Solution:
    """Naive approach using built-in sorted() with key function."""

    def __init__(self, strings: List[str]):
        """Initialize with the list of strings to sort.
        
        Args:
            strings: A list of strings to sort by first 3 characters.
        """
        self.strings = strings

    def merge_sort_substring(self) -> List[str]:
        """Sort strings by their first 3 characters using built-in sort.
        
        Uses Python's sorted() function with a key function that extracts
        the first 3 characters (or the entire string if shorter).
        
        Returns:
            A new sorted list of strings.
        """
        return sorted(self.strings, key=lambda s: s[:3])


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
        instance = SolutionClass(list(case.strings))
        result = instance.merge_sort_substring()
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
