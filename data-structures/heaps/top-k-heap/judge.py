import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import load_classes, run_tests
from tests.cases import TEST_CASES

def run_case_logic(TopKHeap, case):
    """Run test case for TopKHeap."""
    tk = TopKHeap(3)
    for x in [7, 5, 3, 8, 1, 9, 2]:
        tk.insert(x)
    assert tk.A == [1, 2, 3], f"Expected [1, 2, 3], got {tk.A}"
    return True

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    solutions_dir = os.path.join(base_dir, 'solutions')

    # Load and test reference solutions
    reference_solutions = load_classes(solutions_dir, 'TopKHeap', 'reference')
    run_tests(reference_solutions, TEST_CASES, run_case_logic, 'REFERENCE SOLUTIONS')
    
    # Load and test contributed solutions
    contributed_solutions = load_classes(solutions_dir, 'TopKHeap', 'contributed')
    run_tests(contributed_solutions, TEST_CASES, run_case_logic, 'CONTRIBUTED SOLUTIONS')
if __name__ == '__main__':
    main()
