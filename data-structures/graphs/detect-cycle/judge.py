import sys
import os

# Add parent directory to path to allow importing solutions and tests
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    )
)

from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES


def run_case_logic(SolutionClass, case) -> bool:
    """
    Executes a single test case using the provided SolutionClass.
    Returns True if the test passes, False otherwise.
    """
    try:
        instance = SolutionClass()

        result = instance.has_cycle(case.graph)

        if result == case.expected:
            return True
        else:
            print(f"    Expected: {case.expected}")
            print(f"    Got:      {result}")
            return False

    except Exception as e:
        print(f"    Error executing case: {e}")
        return False


if __name__ == "__main__":
    sys.exit(run_judge_from_file(__file__, TEST_CASES, run_case_logic))
