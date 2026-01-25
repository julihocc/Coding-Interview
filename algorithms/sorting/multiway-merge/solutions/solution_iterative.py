import heapq

class Solution:
    """Iterative k-way merge using a Min-Heap."""

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def kWayMerge(self):
        min_heap = []
        
        # Initialize heap with the first element of each non-empty list
        # Heap elements: (value, list_index, element_index)
        for i, lst in enumerate(self.list_of_lists):
            if lst:
                heapq.heappush(min_heap, (lst[0], i, 0))
                
        result = []
        
        while min_heap:
            val, list_idx, elem_idx = heapq.heappop(min_heap)
            result.append(val)
            
            # If there is a next element in the same list, push it to heap
            if elem_idx + 1 < len(self.list_of_lists[list_idx]):
                next_val = self.list_of_lists[list_idx][elem_idx + 1]
                heapq.heappush(min_heap, (next_val, list_idx, elem_idx + 1))
                
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
        instance = SolutionClass(case.lists)
        result = instance.kWayMerge()
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
