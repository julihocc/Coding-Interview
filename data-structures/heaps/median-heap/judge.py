import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES

def run_case_logic(SolutionClass, case):
    """Test a single case for median heap."""
    mh = SolutionClass()
    mh.insert(1); assert mh.get_median() == 1
    mh.insert(2); assert mh.get_median() == 1.5
    mh.insert(3); assert mh.get_median() == 2
    mh.insert(4); assert mh.get_median() == 2.5
    mh.insert(5); assert mh.get_median() == 3
    return True

if __name__ == '__main__':
    run_judge_from_file(__file__, TEST_CASES, run_case_logic)
