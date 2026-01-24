import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES

def run_case_logic(SolutionClass, case):
    """Test a single case for max heap."""
    h = SolutionClass()
    h.insert(5); assert h.max_element()==5
    h.insert(2); assert h.max_element()==5
    h.insert(4); assert h.max_element()==5
    h.insert(-1); assert h.max_element()==5
    h.insert(7); assert h.max_element()==7
    h.delete_max(); assert h.max_element()==5
    h.delete_max(); assert h.max_element()==4
    h.delete_max(); assert h.max_element()==2
    h.delete_max(); assert h.max_element()==-1
    h.delete_max(); assert h.size()==0
    return True

if __name__ == '__main__':
    run_judge_from_file(__file__, TEST_CASES, run_case_logic)
