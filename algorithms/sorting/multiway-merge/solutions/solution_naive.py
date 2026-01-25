class Solution:
    """Flatten all lists, then sort."""

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def kWayMerge(self):
        combined = []
        for lst in self.list_of_lists:
            combined.extend(lst)
        return sorted(combined)

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
        instance = SolutionClass(case.lists)
        result = instance.kWayMerge()
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
