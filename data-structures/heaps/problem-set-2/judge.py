import sys
import os

# Add the project root to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import load_solutions, run_tests
from tests.cases import TEST_CASES

def run_case_logic(sol_func, case):
    # solutions implement a `solve()` function which runs internal asserts.
    # we call it with no args; success is indicated by returning True or
    # by not raising an exception.
    res = sol_func()
    # If the solver returns a boolean, use it; otherwise assume success.
    if isinstance(res, bool):
        return res
    return True

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    solutions_dir = os.path.join(base_dir, 'solutions')

    # Look for `solve` in solution modules
    solutions = load_solutions(solutions_dir, 'solve')
    run_tests(solutions, TEST_CASES, run_case_logic)

if __name__ == '__main__':
    main()
