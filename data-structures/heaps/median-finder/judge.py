import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

from utils.judge_utils import run_judge_from_file
from tests.cases import TEST_CASES


def run_case_logic(SolutionClass, case):
    """Test a single case for Median Finder."""
    mf = SolutionClass()

    for i, num in enumerate(case["inputs"]):
        mf.addNum(num)
        ans = mf.findMedian()
        expected_ans = case["expected"][i]

        if ans != expected_ans:
            print(
                f"Error after inserting {num} (step {i + 1}). Expected: {expected_ans}, Got: {ans}"
            )
            return False

    return True


if __name__ == "__main__":
    run_judge_from_file(__file__, TEST_CASES, run_case_logic)
