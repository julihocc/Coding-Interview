import random
from typing import List


class Solution:
    """Average-case linear-time quickselect with recursive partitioning."""

    def __init__(self, nums: List[int]):
        if not nums:
            raise ValueError("nums must be non-empty")
        self.nums = nums

    def quickselect(self, k: int) -> int:
        return self._quickselect_recursive(0, len(self.nums) - 1, k)
        
    def _quickselect_recursive(self, left: int, right: int, k: int) -> int:
        if left == right:
            return self.nums[left]
            
        pivot_index = random.randint(left, right)
        pivot_index = self._partition(left, right, pivot_index)
        
        if pivot_index == k:
            return self.nums[pivot_index]
        elif k < pivot_index:
            return self._quickselect_recursive(left, pivot_index - 1, k)
        else:
            return self._quickselect_recursive(pivot_index + 1, right, k)

    def _partition(self, left: int, right: int, pivot_index: int) -> int:
        pivot_value = self.nums[pivot_index]
        self.nums[pivot_index], self.nums[right] = self.nums[right], self.nums[pivot_index]
        store_index = left

        for i in range(left, right):
            if self.nums[i] < pivot_value:
                self.nums[store_index], self.nums[i] = self.nums[i], self.nums[store_index]
                store_index += 1

        self.nums[right], self.nums[store_index] = self.nums[store_index], self.nums[right]
        return store_index

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
        instance = SolutionClass(list(case.nums))
        result = instance.quickselect(case.k)
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
