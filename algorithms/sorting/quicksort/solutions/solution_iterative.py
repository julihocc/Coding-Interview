import random
from typing import List


class InPlaceRandomizedQuicksort:
    """In-place quicksort using an explicit stack (Iterative)."""

    def __init__(self, nums: List[int]):
        self.nums = nums

    def quicksort(self) -> List[int]:
        if len(self.nums) < 2:
            return self.nums

        stack = [(0, len(self.nums) - 1)]
        
        while stack:
            low, high = stack.pop()
            
            if low < high:
                pivot_pos = self._partition(low, high)
                
                # Push ranges to stack.
                # Optimization: Push larger range first to minimize stack depth?
                # For basic correctness, order doesn't strictly matter for non-tail-recursion elimination.
                if pivot_pos - 1 > low:
                    stack.append((low, pivot_pos - 1))
                if pivot_pos + 1 < high:
                    stack.append((pivot_pos + 1, high))
                    
        return self.nums

    def _partition(self, low: int, high: int) -> int:
        pivot_index = random.randint(low, high)
        self.nums[pivot_index], self.nums[high] = self.nums[high], self.nums[pivot_index]
        pivot = self.nums[high]
        i = low

        for j in range(low, high):
            if self.nums[j] <= pivot:
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
                i += 1

        self.nums[i], self.nums[high] = self.nums[high], self.nums[i]
        return i

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
        result = instance.quicksort()
        return result == sorted(case.nums)
    
    test_solution(InPlaceRandomizedQuicksort, TEST_CASES, run_case_logic)
