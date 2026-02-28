"""
Local testing script for Network Concept BFS.

Run this script directly to test your solution:
    python judge.py
"""

import sys
import os

# Add the project root to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
problem_dir = current_dir
project_root = os.path.dirname(os.path.dirname(os.path.dirname(problem_dir)))
sys.path.append(project_root)

from utils.judge_utils import test_solution
from tests.cases import TEST_CASES
from solutions.solution import Solution


def run_case_logic(SolutionClass, case):
    """
    Executes the solution for a specific test case.

    Args:
        SolutionClass: The class containing the solution (e.g., Solution).
        case: A test case definition (TestCase).

    Returns:
        bool: True if the test passes, False otherwise.
    """
    instance = SolutionClass()
    tree, root = case.input
    result = instance.bfs(tree, root)
    return result == case.expected


if __name__ == "__main__":
    test_solution(Solution, TEST_CASES, run_case_logic)
