
class Solution:
    """Pairwise merge with recursive reduction to a single list."""

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def kWayMerge(self):
        k = len(self.list_of_lists)
        if k == 0:
            return []
        if k == 1:
            return self.list_of_lists[0]
        merged_lists = self._one_step(self.list_of_lists)
        return Solution(merged_lists).kWayMerge()

    def _one_step(self, list_of_lists):
        if len(list_of_lists) <= 1:
            return list_of_lists
        merged_lists = []
        k = len(list_of_lists)
        for i in range(0, k, 2):
            if i < k - 1:
                merged_lists.append(self._merge_two(list_of_lists[i], list_of_lists[i + 1]))
            else:
                merged_lists.append(list_of_lists[k - 1])
        return merged_lists

    def _merge_two(self, lst1, lst2):
        i = 0
        j = 0
        merged = []

        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                merged.append(lst1[i])
                i += 1
            else:
                merged.append(lst2[j])
                j += 1

        if i < len(lst1):
            merged.extend(lst1[i:])
        if j < len(lst2):
            merged.extend(lst2[j:])
        return merged

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
