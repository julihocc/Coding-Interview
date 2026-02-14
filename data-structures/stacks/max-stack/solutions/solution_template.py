from typing import Optional


class Solution:
    """Template for MaxStack: A stack supporting O(1) maximum retrieval.
    
    Design a stack that supports push, pop, top, and retrieving the 
    maximum element in constant time.
    
    Operations:
        - push(x): Push element x onto stack
        - pop(): Remove the element on top of the stack
        - top(): Get the top element
        - get_max(): Retrieve the maximum element in O(1) time
    
    Example:
        stack = Solution()
        stack.push(1)
        stack.push(5)
        stack.push(3)
        stack.get_max()  # Returns 5
        stack.pop()
        stack.top()      # Returns 5
        stack.get_max()  # Returns 5
    """

    def __init__(self):
        """Initialize your data structure here.
        
        Hints:
            - You'll need the main stack to store elements
            - How can you track the maximum without scanning the entire stack?
            - Consider using an auxiliary data structure
            - What information do you need to maintain when elements are pushed/popped?
        """
        # TODO: Initialize your data structures
        raise NotImplementedError("Initialization not implemented yet")

    def push(self, x: int) -> None:
        """Push element x onto stack.
        
        Args:
            x: Integer to push onto the stack
        
        Hints:
            - Add to main stack
            - How do you update maximum tracking when a new element arrives?
            - Should you always update the maximum tracker?
        
        Time complexity goal: O(1)
        """
        # TODO: Implement push operation
        raise NotImplementedError("Push not implemented yet")

    def pop(self) -> None:
        """Remove the element on top of the stack.
        
        Hints:
            - Remove from main stack
            - What happens to your maximum if you pop the current maximum element?
            - How can you maintain maximum information after removal?
        
        Time complexity goal: O(1)
        """
        # TODO: Implement pop operation
        raise NotImplementedError("Pop not implemented yet")

    def top(self) -> Optional[int]:
        """Get the top element.
        
        Returns:
            The top element of the stack, or None if empty
        
        Time complexity goal: O(1)
        """
        # TODO: Implement top operation
        raise NotImplementedError("Top not implemented yet")

    def get_max(self) -> Optional[int]:
        """Retrieve the maximum element in the stack.
        
        Returns:
            The maximum element, or None if stack is empty
        
        Hints:
            - This should NOT scan the entire stack
            - How can you maintain maximum information efficiently?
            - Think about what happens when maximum elements are pushed/popped
        
        Time complexity goal: O(1)
        Space complexity goal: O(n)
        """
        # TODO: Implement get_max operation
        raise NotImplementedError("Get_max not implemented yet")


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
    
    # Uncomment to test your solution:
    # test_solution(Solution, TEST_CASES, run_case_logic)
