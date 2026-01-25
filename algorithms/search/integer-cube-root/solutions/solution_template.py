"""TEMPLATE: Class-based solution for Integer Cube Root

Implement a class whose name reflects the strategy.
Judges instantiate your class with n in __init__ and call the method.

Reference: See ../README.md for full problem description
"""


class YourCubeRootFinder:
    """Rename and implement this class to match your approach.
    
    Example strategies: LinearCubeRootFinder, BinarySearchCubeRootFinder
    """

    def __init__(self, n):
        """Initialize with the target number.
        
        Args:
            n: A positive integer to find the cube root of.
        """
        assert n > 0, "n must be a positive integer"
        self.n = n

    def integerCubeRoot(self):
        """Find the largest k such that k^3 <= n.
        
        Expected behavior:
        - Return the largest integer k where k * k * k <= self.n
        - For n=8, return 2 (since 2^3 = 8)
        - For n=9, return 2 (since 2^3 = 8 < 9 but 3^3 = 27 > 9)
        
        Hint: Use binary search with _helper method for efficiency.
        
        Returns:
            The largest integer k where k^3 <= n.
        """
        # TODO: Implement search strategy (handle small cases separately if needed)
        # Consider: Linear scan or recursive binary search with _helper method
        raise NotImplementedError
    
    def _helper(self, left: int, right: int) -> int:
        """Recursive binary search helper for cube root.
        
        Args:
            left: Left boundary of search range.
            right: Right boundary of search range.
            
        Returns:
            The cube root within the range [left, right].
        """
        # TODO: Implement recursive refinement logic
        # Use cube operations to compare and narrow the range
        raise NotImplementedError("Recursive helper not implemented yet")

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
        instance = SolutionClass(case.n)
        result = instance.integerCubeRoot()
        return result == case.expected
    
    test_solution(YourCubeRootFinder, TEST_CASES, run_case_logic)
