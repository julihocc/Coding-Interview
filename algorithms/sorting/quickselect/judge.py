import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import load_classes, run_tests
from tests.cases import TEST_CASES

def run_case_logic(SolutionClass, case):
    instance = SolutionClass(list(case.nums))
    result = instance.quickselect(case.k)
    return result == case.expected

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    solutions_dir = os.path.join(base_dir, 'solutions')

    # Load all solutions (from solutions/solution_*.py)
    solutions = load_classes(
        solutions_dir, "Solution", subfolder=None, file_pattern="solution_*.py"
    )
    run_tests(solutions, TEST_CASES, run_case_logic, 'SOLUTIONS')

if __name__ == "__main__":
    main()
