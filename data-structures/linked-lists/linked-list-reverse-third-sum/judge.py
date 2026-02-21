import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES


def run_case_logic(SolutionClass, case):
    """Test a single reverse-third-sum case.

    Args:
        SolutionClass: The Solution class to test.
        case: TestCase with input_values and expected_sum.

    Returns:
        True if find_sum() matches expected_sum, False otherwise.
    """
    instance = SolutionClass()
    head = instance.build(case.input_values)
    return instance.find_sum(head) == case.expected_sum


if __name__ == "__main__":
    run_judge_from_file(__file__, TEST_CASES, run_case_logic)
