import os
import sys

from tests.cases import TEST_CASES

# Add the root directory to sys.path to allow importing utils
script_dir = os.path.dirname(__file__)
ROOT_DIR = os.path.abspath(os.path.join(script_dir, "../../../"))
sys.path.append(ROOT_DIR)

from utils import judge_utils  # noqa: E402


def run_test_case(sol_func, case):
    """
    Runner function for a single test case.
    """
    result = sol_func(case.nums, case.target)
    return result == case.expected


def main():
    """
    Main function to run tests for Search Insert Position.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    solutions_dir = os.path.join(current_dir, "solutions")

    # Load solutions that have the 'search_insert' function
    solutions = judge_utils.load_solutions(
        solutions_dir, "search_insert", subfolder="reference"
    )

    # Run tests
    judge_utils.run_tests(
        solutions, TEST_CASES, run_test_case, section_name="Search Insert Position"
    )


if __name__ == "__main__":
    main()
