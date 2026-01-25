"""TEMPLATE: Class-based solution for Find Crossover Indices

Implement a class whose name reflects the strategy.
Judges instantiate your class with x, y in __init__ and call the method.

Reference: See ../README.md for full problem description
"""


class Solution:
    """Rename and implement this class to match your approach.
    
    Example strategies: LinearScanCrossoverFinder, BinarySearchCrossoverFinder
    """

    def __init__(self, x, y):
        """Initialize with two sorted arrays.
        
        Args:
            x: First sorted list of integers.
            y: Second sorted list of integers (same length as x).
        """
        assert len(x) == len(y), "Arrays must have equal length"
        self.x = x
        self.y = y

    def findCrossoverIndex(self):
        """Find the crossover index where x[i] >= y[i] but x[i+1] < y[i+1].
        
        Expected behavior:
        - Return index i where self.x[i] >= self.y[i] AND self.x[i+1] < self.y[i+1]
        - Return -1 if no such crossover exists
        - The crossover is the point where x transitions from below y to above y
        
        Hint: Use a helper method for recursive binary search refinement.
            
        Returns:
            The crossover index, or -1 if no crossover exists.
        """
        # TODO: Implement search strategy
        # Consider: Linear scan or recursive binary search with _helper method
        raise NotImplementedError("Search strategy not implemented yet")
    
    def _helper(self, left: int, right: int) -> int:
        """Recursive helper for binary search refinement.
        
        Args:
            left: Left boundary of search range.
            right: Right boundary of search range.
            
        Returns:
            The crossover index within the range [left, right].
        """
        # TODO: Implement recursive refinement logic
        raise NotImplementedError("Recursive helper not implemented yet")

if __name__ == "__main__":
    import sys
    import os

    # Add the project root to sys.path
    # Current file: .../algorithms/search/find-crossover-indices/solutions/solution_template.py
    # Root: .../
    current_dir = os.path.dirname(os.path.abspath(__file__))
    problem_dir = os.path.dirname(current_dir)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(problem_dir)))
    
    sys.path.append(project_root)
    sys.path.append(problem_dir)

    from utils.judge_utils import test_solution
    from tests.cases import TEST_CASES

    def run_case_logic(SolutionClass, case):
        instance = SolutionClass(list(case.x), list(case.y))
        result = instance.findCrossoverIndex()
        if isinstance(case.expected, list):
             return result in case.expected
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
