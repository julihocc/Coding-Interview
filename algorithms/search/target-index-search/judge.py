import sys
import os

# Add the parent directory (project root) to sys.path import hackerrank.judge_utils
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import load_solutions, run_tests
from tests.cases import TEST_CASES

def run_case_logic(sol_func, case):
    result = sol_func(case.nums, case.target)
    return result == case.expected

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    solutions_dir = os.path.join(base_dir, 'solutions')
    
    solutions = load_solutions(solutions_dir, 'target_index_search')
    run_tests(solutions, TEST_CASES, run_case_logic)

if __name__ == "__main__":
    main()
