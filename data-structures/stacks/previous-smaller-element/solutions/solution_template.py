from typing import List


class Solution:
    """Template for finding the previous smaller element for each element in an array.
    
    Problem: Given an array of integers, for each element find the most recent
    previous element that is smaller. Return -1 if no such element exists.
    
    Example:
        Input: [4, 5, 2, 10, 8]
        Output: [-1, 4, -1, 2, 2]
        
        Explanation:
        - 4: no previous smaller element → -1
        - 5: previous smaller is 4
        - 2: no previous smaller element → -1
        - 10: previous smaller is 2
        - 8: previous smaller is 2
    """

    def __init__(self, numbers: List[int]):
        """Initialize with the input array.
        
        Args:
            numbers: List of integers to process
        """
        self.numbers = numbers

    def find_previous_smaller(self) -> List[int]:
        """Find the previous smaller element for each element in the array.
        
        Returns:
            List of integers where each element is either:
            - The most recent previous smaller element
            - -1 if no such element exists
        
        Hints:
            - Naive approach: For each element, scan backwards to find smaller element
            - Optimized approach: Use a stack to maintain potential candidates
            - Think about which elements can never be "previous smaller" for future elements
            - When you encounter a number, larger elements on the stack are no longer useful
        
        Time complexity goal: O(n)
        Space complexity goal: O(n)
        """
        # TODO: Implement your solution here
        raise NotImplementedError("Solution not implemented yet")


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
    
    # Uncomment to test your solution:
    # test_solution(Solution, TEST_CASES, run_case_logic)
