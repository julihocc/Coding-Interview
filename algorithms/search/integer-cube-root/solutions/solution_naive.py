class Solution:
    """Linear search for the largest k with k^3 <= n."""

    def __init__(self, n):
        self.n = n

    def integerCubeRoot(self):
        if self.n == 0:
            return 0
        if self.n < 0:
            return -Solution(-self.n).integerCubeRoot()

        k = 1
        while (k + 1) ** 3 <= self.n:
            k += 1
        return k

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
