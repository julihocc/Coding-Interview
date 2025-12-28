import sys
import os

# Add the project root to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import load_solutions, run_tests
from tests.cases import TEST_CASES

def run_case_logic(sol_func, case):
    """Run test case for MinHeap."""
    MinHeap = sol_func()
    
    h = MinHeap()
    h.insert(5); assert h.min_element()==5
    h.insert(2); assert h.min_element()==2
    h.insert(4); assert h.min_element()==2
    h.insert(-1); assert h.min_element()==-1
    h.insert(7); assert h.min_element()==-1
    h.delete_min(); assert h.min_element()==2
    h.delete_min(); assert h.min_element()==4
    h.delete_min(); assert h.min_element()==5
    h.delete_min(); assert h.min_element()==7
    h.delete_min(); assert h.size()==0
    return True

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    solutions_dir = os.path.join(base_dir, 'solutions')

    # Each solution file exports a single `solve` entrypoint
    solutions = load_solutions(solutions_dir, 'solve')
    run_tests(solutions, TEST_CASES, run_case_logic)

if __name__ == '__main__':
    main()
