"""TEMPLATE: Class-based solution for Multiway Merge

Implement a class whose name reflects the strategy (e.g., PairwiseMergeKWay).
Judges instantiate your class with list_of_lists in __init__ and call the method.

Reference: See ../README.md for full problem description
"""

from typing import List


class Solution:
    """Rename and implement this class to match your approach.
    
    Example strategies: FlatSortMerger, PairwiseMergeKWay
    """

    def __init__(self, list_of_lists: List[List[int]]):
        """Initialize with k sorted lists.
        
        Args:
            list_of_lists: A list of k sorted lists to merge.
        """
        self.list_of_lists = list_of_lists

    def kWayMerge(self) -> List[int]:
        """Merge k sorted lists into a single sorted list.
        
        Expected behavior:
        - Return a single sorted list containing all elements from input lists
        - Preserve relative order for equal elements (stable merge)
        - Handle edge cases: empty lists, single list, lists of different lengths
        
        Hint: Consider pairwise merging with recursion for divide-and-conquer.
              Use _one_step and _merge_two helper methods.
        
        Returns:
            A single sorted list with all elements from self.list_of_lists.
        """
        # TODO: Implement merge strategy
        # Consider: Flat sort vs. pairwise merge with recursive reduction
        raise NotImplementedError("Merge strategy not implemented yet")
    
    def _one_step(self, list_of_lists: List[List[int]]) -> List[List[int]]:
        """Perform one round of pairwise merging.
        
        Merge pairs of adjacent lists to reduce count.
        If odd number of lists, last list remains unmerged.
        
        Args:
            list_of_lists: Current list of lists to process.
            
        Returns:
            A new list of merged results (approximately half the size).
        """
        # TODO: Iterate through list_of_lists, merging pairs
        # Handle odd-length case by passing last list unchanged
        raise NotImplementedError("One step helper not implemented yet")
    
    def _merge_two(self, lst1: List[int], lst2: List[int]) -> List[int]:
        """Merge two sorted lists into a single sorted list.
        
        Args:
            lst1: First sorted list.
            lst2: Second sorted list.
            
        Returns:
            A single sorted list containing all elements from lst1 and lst2.
        """
        # TODO: Use two pointers to merge lists in linear time
        # Compare elements from both lists and append smaller one
        raise NotImplementedError("Merge two helper not implemented yet")

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
        # The test case has 'lists' but the class expects 'list_of_lists'
        instance = SolutionClass(list(case.lists))
        result = instance.kWayMerge()
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
