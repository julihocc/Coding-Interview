import os
import sys

from tests.cases import TEST_CASES

# Add the root directory to sys.path to allow importing utils
script_dir = os.path.dirname(__file__)
ROOT_DIR = os.path.abspath(os.path.join(script_dir, "../../../"))
sys.path.append(ROOT_DIR)

from utils.judge_utils import run_judge_from_file  # noqa: E402


def run_test_case(sol_class, case):
    """Test a single case for browser history pre-order traversal."""
    sol = sol_class()
    result = sol.pre_order(case.root)
    return result == case.expected


if __name__ == "__main__":
    run_judge_from_file(__file__, TEST_CASES, run_test_case, section_name="Solutions")
