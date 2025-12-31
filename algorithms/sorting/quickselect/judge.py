import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import load_classes_with_method, run_tests
from tests.cases import TEST_CASES

def run_case_logic(SolutionClass, case):
    instance = SolutionClass()
    result = instance.quickselect(list(case.nums), case.k)
    return result == case.expected

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    solutions_dir = os.path.join(base_dir, 'solutions')

    # Load and test reference solutions
    reference_solutions = load_classes_with_method(solutions_dir, 'quickselect', 'reference')
    run_tests(reference_solutions, TEST_CASES, run_case_logic, 'REFERENCE SOLUTIONS')
    
    # Load and test contributed solutions
    contributed_solutions = load_classes_with_method(solutions_dir, 'quickselect', 'contributed')
    run_tests(contributed_solutions, TEST_CASES, run_case_logic, 'CONTRIBUTED SOLUTIONS')
if __name__ == "__main__":
    main()
