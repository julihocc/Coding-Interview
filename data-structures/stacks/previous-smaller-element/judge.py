import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES

def run_case_logic(SolutionClass, case):
    """Test a single case for previous smaller element."""
    instance = SolutionClass(case.numbers)
    result = instance.find_previous_smaller()
    return result == case.expected

if __name__ == "__main__":
    run_judge_from_file(__file__, TEST_CASES, run_case_logic)
