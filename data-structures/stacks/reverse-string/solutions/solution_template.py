"""TEMPLATE: Function-based solution for Reverse String using Stack

Reference: See ../README.md for full problem description
"""

class Solution:
    def reverse_string(self, s: str) -> str:
        """Reverse the input string using a stack.

        Args:
            s: The string to reverse.

        Returns:
            The reversed string.
        """
        # TODO: Implement your solution here.
        # Remember to use a stack (list in Python) to reverse the string.
        raise NotImplementedError("Solution not implemented yet")
        return ""

if __name__ == "__main__":
    import sys
    import os

    # Add the project root to sys.path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    problem_dir = os.path.dirname(current_dir)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(problem_dir)))
    
    sys.path.append(project_root)
    sys.path.append(problem_dir)

    from utils.judge_utils import test_solution
    from tests.cases import TEST_CASES

    def run_case_logic(SolutionClass, case):
        instance = SolutionClass()
        result = instance.reverse_string(case.input_str)
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
