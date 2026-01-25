class Solution:
    """Binary search to find the largest k with k^3 <= n."""

    def __init__(self, n):
        assert n > 0
        self.n = n

    def integerCubeRoot(self):
        if self.n == 1:
            return 1
        if self.n == 2:
            return 1
        return self._helper(0, self.n - 1)

    def _helper(self, left, right):
        cube = lambda x: x * x * x
        assert left < right
        mid = (left + right) // 2

        if cube(mid) <= self.n and cube(mid + 1) > self.n:
            return mid
        if cube(mid) > self.n:
            return self._helper(left, mid)
        return self._helper(mid, right)

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
    
    test_solution(Solution, TEST_CASES, run_case_logic)
