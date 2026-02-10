from typing import List


class Solution:
    """Naive O(n^2) approach comparing each element with all previous elements."""

    def __init__(self, numbers: List[int]):
        self.numbers = numbers

    def find_previous_smaller(self) -> List[int]:
        """Find the previous smaller element for each element in the array.
        
        For each element, scan backwards through all previous elements
        to find the first smaller one.
        
        Time complexity: O(n^2)
        Space complexity: O(n) for the result array
        """
        result = []
        
        for i in range(len(self.numbers)):
            # Search backwards for a smaller element
            found = -1
            for j in range(i - 1, -1, -1):
                if self.numbers[j] < self.numbers[i]:
                    found = self.numbers[j]
                    break
            result.append(found)
        
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
