"""Queue implementation using Python list (Naive approach).

This approach uses a Python list with pop(0) for dequeue operations,
which has O(n) time complexity due to element shifting.

Time Complexity:
    - enqueue: O(1)
    - dequeue: O(n) - requires shifting all elements
    - peek: O(1)
    - is_empty: O(1)
    - size: O(1)
    
Space Complexity: O(n) where n is the number of elements
"""


class Solution:
    """Queue implementation using Python list."""
    
    def __init__(self):
        """Initialize an empty queue using a list."""
        self.queue = []
    
    def enqueue(self, element):
        """Add an element to the end of the queue.
        
        Args:
            element: The element to add to the queue
        """
        self.queue.append(element)
    
    def dequeue(self):
        """Remove and return the element from the front of the queue.
        
        Returns:
            The element at the front of the queue
            
        Note: This operation is O(n) because pop(0) requires shifting
        all remaining elements.
        """
        if not self.is_empty():
            return self.queue.pop(0)
        return None
    
    def peek(self):
        """Return the element at the front without removing it.
        
        Returns:
            The element at the front of the queue
        """
        if not self.is_empty():
            return self.queue[0]
        return None
    
    def is_empty(self):
        """Check if the queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise
        """
        return len(self.queue) == 0
    
    def size(self):
        """Return the number of elements in the queue.
        
        Returns:
            int: The number of elements in the queue
        """
        return len(self.queue)


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
        queue = SolutionClass()
        
        for i, operation in enumerate(case.operations):
            args = case.arguments[i]
            expected = case.expected[i]
            
            if operation == "enqueue":
                result = queue.enqueue(*args)
            elif operation == "dequeue":
                result = queue.dequeue()
            elif operation == "peek":
                result = queue.peek()
            elif operation == "is_empty":
                result = queue.is_empty()
            elif operation == "size":
                result = queue.size()
            else:
                return False
            
            if result != expected:
                return False
        
        return True
    
    test_solution(Solution, TEST_CASES, run_case_logic)
