import sys
import os

# Add the parent directory (project root) to sys.path allow importing hackerrank.judge_utils
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir)) # Up to 'dev/' (or wherever 'hackerrank' sits)
# Wait, 'hackerrank' is a package? The structure is:
# dev/hackerrank/judge_utils.py
# dev/hackerrank/left-rotation/judge.py
# To import `hackerrank.judge_utils`, we need `dev` in sys.path.
# `current_dir` = .../left-rotation
# `os.path.dirname(current_dir)` = .../hackerrank
# `os.path.dirname(...)` = .../dev (repo root in this context)
sys.path.append(os.path.dirname(os.path.dirname(current_dir)))

from hackerrank.judge_utils import load_solutions, run_tests
from tests.cases import TEST_CASES

def run_case_logic(sol_func, case):
    # Pass copy of a to ensure isolation
    result = sol_func(list(case.a), case.d)
    return result == case.expected

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    solutions_dir = os.path.join(base_dir, 'solutions')
    
    solutions = load_solutions(solutions_dir, 'rotLeft')
    run_tests(solutions, TEST_CASES, run_case_logic)

if __name__ == "__main__":
    main()
