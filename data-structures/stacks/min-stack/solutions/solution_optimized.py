from typing import Optional


class Solution:
    """Optimized MinStack using auxiliary stack for O(1) get_min.
    
    Time complexity:
        - push: O(1)
        - pop: O(1)
        - top: O(1)
        - get_min: O(1)
    
    Space complexity: O(n) for both stacks
    """

    def __init__(self):
        """Initialize two stacks: main stack and min tracking stack."""
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        """Push element x onto stack and update minimum tracker.
        
        If x is smaller than or equal to current minimum,
        also push it onto min_stack.
        """
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        """Remove the element on top of the stack.
        
        If the popped element is the current minimum,
        also pop from min_stack.
        """
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> Optional[int]:
        """Get the top element.
        
        Returns None if stack is empty.
        """
        return self.stack[-1] if self.stack else None

    def get_min(self) -> Optional[int]:
        """Retrieve the minimum element in O(1) time.
        
        The top of min_stack always contains the current minimum.
        Returns None if stack is empty.
        """
        return self.min_stack[-1] if self.min_stack else None


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
