import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES


def run_case_logic(SolutionClass, case):
    """Test a single insert-after-head case.

    Args:
        SolutionClass: The Solution class to test
        case: TestCase with push_values, insert_values, expected_list

    Returns:
        True if to_list() matches expected_list, False otherwise.
    """
    instance = SolutionClass()

    # push() prepends, so push in order to build the intended list
    for value in case.push_values:
        instance.push(value)

    # insert_after_head() each value in sequence
    for value in case.insert_values:
        instance.insert_after_head(value)

    return instance.to_list() == case.expected_list


if __name__ == "__main__":
    run_judge_from_file(__file__, TEST_CASES, run_case_logic)
