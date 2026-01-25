class Solution:
    """Linear scan from the right to locate the crossover index."""

    def __init__(self, x, y):
        assert len(x) == len(y)
        self.x = x
        self.y = y

    def findCrossoverIndex(self):
        n = len(self.x)

        for i in range(n - 1, -1, -1):
            if self.x[i] >= self.y[i]:
                return i

        return -1

if __name__ == "__main__":
    import sys
    import os

    # Add the project root to sys.path
    # Current file: .../algorithms/search/find-crossover-indices/solutions/solution_naive.py
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
