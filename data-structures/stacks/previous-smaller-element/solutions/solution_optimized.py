from typing import List


class Solution:
    """Optimized O(n) approach using a monotonic stack."""

    def __init__(self, numbers: List[int]):
        self.numbers = numbers

    def find_previous_smaller(self) -> List[int]:
        """Find the previous smaller element for each element using a stack.
        
        Maintains a stack of candidates for previous smaller elements.
        Elements that can't be "previous smaller" for any future element
        are removed from the stack.
        
        Time complexity: O(n) - each element is pushed and popped at most once
        Space complexity: O(n) for the stack and result array
        """
        result = []
        stack = []
        
        for num in self.numbers:
            # Remove elements that can't be previous smaller for current or future elements
            while stack and stack[-1] >= num:
                stack.pop()
            
            # Top of stack is the previous smaller element (or -1 if stack is empty)
            result.append(stack[-1] if stack else -1)
            
            # Add current element as potential previous smaller for future elements
            stack.append(num)
        
        return result


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
        instance = SolutionClass(list(case.numbers))
        result = instance.find_previous_smaller()
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
