import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES


def run_case_logic(SolutionClass, case):
    """Test a single case for circular linked list operations.

    Args:
        SolutionClass: The Solution class to test
        case: A TestCase object containing operations and expected results

    Returns:
        True if all operations produce expected results, False otherwise
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

    # Check final list state
    if instance.to_list() != case.expected_list:
        return False

    # Check search results if provided
    if case.search_results:
        for search_value, expected_result in case.search_results:
            if instance.search(search_value) != expected_result:
                return False

    return True


if __name__ == "__main__":
    run_judge_from_file(__file__, TEST_CASES, run_case_logic)
