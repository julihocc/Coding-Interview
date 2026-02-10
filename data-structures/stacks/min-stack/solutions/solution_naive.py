from typing import Optional


class Solution:
    """Naive approach: Recalculate minimum on each get_min() call.
    
    Time complexity:
        - push: O(1)
        - pop: O(1)
        - top: O(1)
        - get_min: O(n)
    """

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        """Push element x onto the stack."""
        self.stack.append(x)

    def pop(self) -> None:
        """Remove the element on top of the stack."""
        if self.stack:
            self.stack.pop()

    def top(self) -> Optional[int]:
        """Get the top element."""
        return self.stack[-1] if self.stack else None

    def get_min(self) -> Optional[int]:
        """Retrieve the minimum element in the stack.
        
        Scans through entire stack to find minimum.
        Time complexity: O(n)
        """
        if not self.stack:
            return None
        return min(self.stack)


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
        stack = SolutionClass()
        results = []
        
        for op, val, expected in zip(case.operations, case.values, case.expected):
            if op == "push":
                result = stack.push(val)
            elif op == "pop":
                result = stack.pop()
            elif op == "top":
                result = stack.top()
            elif op == "get_min":
                result = stack.get_min()
            
            results.append(result)
        
        return results == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
