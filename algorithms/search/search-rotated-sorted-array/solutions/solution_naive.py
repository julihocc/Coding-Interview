class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Searches for a target value in a rotated sorted array using linear search.

        Args:
            nums: The rotated sorted array.
            target: The value to search for.

        Returns:
            The index of the target value if found, otherwise -1.
        """
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1

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
        result = instance.search(list(case.nums), case.target)
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
