class Solution:
    """Iterative binary search to locate the crossover index."""

    def __init__(self, x, y):
        assert len(x) == len(y)
        self.x = x
        self.y = y

    def findCrossoverIndex(self):
        n = len(self.x)
        if n == 0:
            return -1
        
        # Helper logic implemented iteratively
        left, right = 0, n - 1
        
        # Edge case: check bounds akin to recursive base cases or just run binary search
        # The recursive helper handles:
        # if left == right: return left
        # if left + 1 == right: return left
        # mid logic
        
        # We need to maintain the invariant that the crossover is within [left, right]
        # or find the specific index where x[i] >= y[i] is true and x[i+1] < y[i+1] (implicitly)
        # But the problem defines it as largest index i where x[i] >= y[i].
        # The monotonic property suggests x[i] >= y[i] allows us to search right (to find a larger i),
        # but if x[mid] < y[mid], we must search left.
        
        ans = -1
        # To find the LARGEST index, we use a standard pattern:
        # If monotonic condition met, record ans and try to go Right.
        # Else, go Left.
        
        while left <= right:
            mid = (left + right) // 2
            
            if self.x[mid] >= self.y[mid]:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans

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
        instance = SolutionClass(list(case.x), list(case.y))
        result = instance.findCrossoverIndex()
        if isinstance(case.expected, list):
             return result in case.expected
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
