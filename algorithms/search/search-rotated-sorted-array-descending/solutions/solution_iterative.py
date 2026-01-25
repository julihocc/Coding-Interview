from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Search in a rotated sorted array (descending) using binary search.
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
                
            # Left Side is Sorted (Descending)
            # e.g. [9, 8, 7, 1, 15, ...]  mid=1 (8), left=0 (9). 9 >= 8.
            if nums[left] >= nums[mid]:
                # Check if target is in the left sorted portion
                if nums[left] >= target > nums[mid]:
                    # Go Left
                    right = mid - 1
                else:
                    # Go Right (pivot is to the right)
                    left = mid + 1
            
            # Right Side is Sorted (Descending)
            # e.g. [..., 15, 12, 11]
            else:
                # Check if target is in the right sorted portion
                if nums[mid] > target >= nums[right]:
                    # Go Right
                    left = mid + 1
                else:
                    # Go Left
                    right = mid - 1
                    
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
