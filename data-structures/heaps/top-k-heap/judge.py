import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import load_solutions, run_tests
from tests.cases import TEST_CASES

def run_case_logic(sol_func, case):
    """Run test case for TopKHeap."""
    TopKHeap = sol_func
    
    tk = TopKHeap(3)
    for x in [7, 5, 3, 8, 1, 9, 2]:
        tk.insert(x)
    assert tk.A == [1, 2, 3], f"Expected [1, 2, 3], got {tk.A}"
    return True

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    solutions_dir = os.path.join(base_dir, 'solutions')

    solutions = load_solutions(solutions_dir, 'solve')
    run_tests(solutions, TEST_CASES, run_case_logic)

if __name__ == '__main__':
    main()
