import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES

def run_case_logic(SolutionClass, case):
    """Test a single case for top-k heap."""
    tk = SolutionClass(3)
    for x in [7, 5, 3, 8, 1, 9, 2]:
        tk.insert(x)
    assert tk.A == [1, 2, 3], f"Expected [1, 2, 3], got {tk.A}"
    return True

if __name__ == '__main__':
    run_judge_from_file(__file__, TEST_CASES, run_case_logic)
