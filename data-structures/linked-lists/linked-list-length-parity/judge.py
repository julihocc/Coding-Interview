import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES


def run_case_logic(SolutionClass, case):
    """Test a single length-parity case.

    Args:
        SolutionClass: The Solution class to test.
        case: TestCase with input_values and expected_parity.

    Returns:
        True if length_parity() matches expected_parity, False otherwise.
    """
    instance = SolutionClass()
    for value in case.input_values:
        instance.add_node(value)
    return instance.length_parity() == case.expected_parity


if __name__ == "__main__":
    run_judge_from_file(__file__, TEST_CASES, run_case_logic)
