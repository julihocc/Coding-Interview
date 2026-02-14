from typing import Optional


class Solution:
    """Optimized MaxStack using auxiliary stack for O(1) get_max.
    
    Time complexity:
        - push: O(1)
        - pop: O(1)
        - top: O(1)
        - get_max: O(1)
    
    Space complexity: O(n) for both stacks
    """

    def __init__(self):
        """Initialize two stacks: main stack and max tracking stack."""
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        """Push element x onto stack and update maximum tracker.
        
        If x is greater than or equal to current maximum,
        also push it onto max_stack.
        """
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self) -> None:
        """Remove the element on top of the stack.
        
        If the popped element is the current maximum,
        also pop from max_stack.
        """
        if self.stack:
            if self.stack[-1] == self.max_stack[-1]:
                self.max_stack.pop()
            self.stack.pop()

    def top(self) -> Optional[int]:
        """Get the top element.
        
        Returns None if stack is empty.
        """
        return self.stack[-1] if self.stack else None

    def get_max(self) -> Optional[int]:
        """Retrieve the maximum element in O(1) time.
        
        The top of max_stack always contains the current maximum.
        Returns None if stack is empty.
        """
        return self.max_stack[-1] if self.max_stack else None


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
            elif op == "get_max":
                result = stack.get_max()
            
            results.append(result)
        
        return results == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
