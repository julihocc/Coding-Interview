import sys
import os

# Add the parent directory (project root) to sys.path allow importing utils.judge_utils
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import load_classes, run_tests
from tests.cases import TEST_CASES

def run_case_logic(SolutionClass, case):
    # Pass copy of a to ensure isolation
    instance = SolutionClass()
    result = instance.rotLeft(list(case.a), case.d)
    return result == case.expected

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    solutions_dir = os.path.join(base_dir, 'solutions')

    solutions = load_classes(
        solutions_dir, "Solution", subfolder=None, file_pattern="solution_*.py"
    )
    run_tests(solutions, TEST_CASES, run_case_logic, 'SOLUTIONS', report_dir=base_dir)
if __name__ == "__main__":
    main()
