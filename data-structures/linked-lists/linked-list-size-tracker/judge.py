import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES


def run_case_logic(SolutionClass, case):
    """Test a single size-tracker case.

    Checks both:
    1. The contents of the list (to_list)
    2. The size counter value
    """
    instance = SolutionClass()

    for operation in case.operations:
        op_name = operation[0]
        op_args = operation[1:]

        if op_name == "insert":
            instance.insert(*op_args)
        elif op_name == "delete":
            instance.delete(*op_args)

    if instance.to_list() != case.expected_list:
        return False

    if instance.size != case.expected_size:
        return False

    return True


if __name__ == "__main__":
    run_judge_from_file(__file__, TEST_CASES, run_case_logic)
