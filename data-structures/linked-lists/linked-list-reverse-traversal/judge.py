import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES


def run_case_logic(SolutionClass, case):
    """Test a single reverse-traversal case.

    Args:
        SolutionClass: The Solution class to test.
        case: TestCase with input_values and expected_output.

    Returns:
        True if to_reverse_list() matches expected_output, False otherwise.
    """
    instance = SolutionClass()

    for value in case.input_values:
        instance.push(value)

    return instance.to_reverse_list() == case.expected_output


if __name__ == "__main__":
    run_judge_from_file(__file__, TEST_CASES, run_case_logic)
