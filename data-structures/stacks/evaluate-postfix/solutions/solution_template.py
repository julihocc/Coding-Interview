"""TEMPLATE: Function-based solution for Evaluate Postfix Expression

Reference: See ../README.md for full problem description
"""

class Solution:
    def eval_rpn(self, tokens: list[str]) -> int:
        """Evaluate the value of an arithmetic expression in Reverse Polish Notation.

        Args:
            tokens: A list of strings representing the expression.

        Returns:
            The integer value of the evaluated expression.
        """
        # TODO: Implement your solution here.
        # Use a stack to evaluate the expression.
        raise NotImplementedError("Solution not implemented yet")
        return 0

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
        result = instance.eval_rpn(case.tokens)
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
