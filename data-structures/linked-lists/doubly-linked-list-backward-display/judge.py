import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES


def run_case_logic(SolutionClass, case):
    """Test a single backward-display case.

    Args:
        SolutionClass: The Solution class to test
        case: TestCase with operations and expected_backward

    Returns:
        True if display_backward() matches expected_backward, False otherwise.
    """
    instance = SolutionClass()

    # Execute all operations
    for operation in case.operations:
        op_name = operation[0]
        op_args = operation[1:]

        if op_name == "insert":
            instance.insert(*op_args)
        elif op_name == "delete":
            instance.delete(*op_args)

    # Validate backward traversal
    if instance.display_backward() != case.expected_backward:
        return False

    return True


if __name__ == "__main__":
    run_judge_from_file(__file__, TEST_CASES, run_case_logic)
