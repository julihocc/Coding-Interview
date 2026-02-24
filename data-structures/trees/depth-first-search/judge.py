import os
import sys

from tests.cases import TEST_CASES

# Add the root directory to sys.path to allow importing utils
script_dir = os.path.dirname(__file__)
ROOT_DIR = os.path.abspath(os.path.join(script_dir, "../../../"))
sys.path.append(ROOT_DIR)

from utils.judge_utils import run_judge_from_file  # noqa: E402


def run_test_case(sol_class, case):
    """Test a single case for DFS tree traversal."""
    sol = sol_class()
    if case.mode == "traversal":
        result = sol.dfs(case.tree, case.start)
        return result == case.expected
    elif case.mode == "path":
        result = sol.find_path(case.tree, case.start, case.end)
        return result == case.expected
    return False


if __name__ == "__main__":
    run_judge_from_file(__file__, TEST_CASES, run_test_case, section_name="Solutions")
