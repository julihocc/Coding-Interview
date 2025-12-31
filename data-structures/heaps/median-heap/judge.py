import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import load_classes, run_tests
from tests.cases import TEST_CASES

def run_case_logic(MedianMaintainingHeap, case):
    """Run test case for MedianMaintainingHeap."""
    mh = MedianMaintainingHeap()
    mh.insert(1); assert mh.get_median() == 1
    mh.insert(2); assert mh.get_median() == 1.5
    mh.insert(3); assert mh.get_median() == 2
    mh.insert(4); assert mh.get_median() == 2.5
    mh.insert(5); assert mh.get_median() == 3
    return True

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    solutions_dir = os.path.join(base_dir, 'solutions')

    solutions = load_classes(solutions_dir, 'MedianMaintainingHeap')
    run_tests(solutions, TEST_CASES, run_case_logic)

if __name__ == '__main__':
    main()
