"""TEMPLATE: Class-based solution for Count Anti-Inversions

Implement a class that counts anti-inversion pairs in an array.
Judges instantiate your class with array data in __init__ and call the method.

Reference: See ../README.md for full problem description
"""

from typing import List


class Solution:
    """Implement your approach to count anti-inversion pairs.
    
    Consider strategies:
    - Naive: O(n²) nested loops checking all pairs
    - Recursive: O(n log n) recursive merge sort
    - Iterative: O(n log n) iterative merge sort
    """

    def __init__(self, arr: List[int]):
        """Initialize with the array to analyze.
        
        Args:
            arr: List of integers (can include negative numbers, duplicates)
                 Range: -10⁹ to 10⁹
                 Length: 1 to 10⁵
        """
        self.arr = arr  # TODO: Consider if you need to copy this

    def count_anti_inversions(self) -> int:
        """Count pairs (i, j) where i < j and arr[i] < arr[j].
        
        Expected behavior:
        - Return 0 for empty or single-element arrays
        - Count only strict inequalities (arr[i] < arr[j], not <=)
        - Consider all pairs where first index comes before second
        
        Examples:
        - [2, 4, 1, 3, 5] → 7 anti-inversions
        - [1, 2, 3] → 3 anti-inversions (all pairs)
        - [3, 2, 1] → 0 anti-inversions (reverse sorted)
        - [3, 3, 3] → 0 anti-inversions (all equal)
        
        Returns:
            Total count of anti-inversion pairs
        """
        # TODO: Implement counting strategy
        print(self.arr)
        ordered_arr, total_anti_inversions = self._merge_sort_and_count(
            self.arr, 0, len(self.arr)-1
        )
        print(total_anti_inversions)
        return total_anti_inversions
    
    def _merge_sort_and_count(self, arr: List[int], left: int, right: int) -> tuple[List[int], int]:
        """Helper: Recursively sort and count anti-inversions.
        
        For merge sort approach: divide array, recursively count in halves,
        then count cross-inversions during merge.
        
        Args:
            arr: Array to sort
            left: Left boundary index
            right: Right boundary index
            
        Returns:
            Tuple of (sorted_subarray, anti_inversion_count)
        """
        # TODO: Implement divide-and-conquer logic
        # Hint: Base case when left >= right
        # Hint: Find mid, recursively count left and right
        # Hint: Merge and count cross-inversions
        if left > right: 
            return [], 0
        
        if left == right:
            return [arr[left]], 0 
        
        mid = (left+right)//2

        left_ordered, left_counter = self._merge_sort_and_count(arr, left, mid) 
        right_ordered, right_counter = self._merge_sort_and_count(arr, mid+1, right) 

        result, new_counter = self._merge_and_count(left_ordered, right_ordered)

        outcome = result, left_counter+new_counter+right_counter
        print(f"  {outcome}")

        return outcome

    
    def _merge_and_count(self, left: List[int], right: List[int]) -> tuple[List[int], int]:
        """Helper: Merge two sorted arrays and count anti-inversions.
        
        Key insight: When taking element from left array, it's smaller
        than all remaining elements in right array, forming anti-inversions.
        
        Args:
            left: Sorted left subarray
            right: Sorted right subarray
            
        Returns:
            Tuple of (merged_sorted_array, anti_inversion_count)
        """
        # TODO: Implement merge logic with counting
        # Hint: Use two pointers, count when taking from left array
        # Hint: How many elements from right form anti-inversions?
        print(f"    {left} {right}")
        i = j = 0 
        result = []
        counter = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]: 
                result.append(left[i])
                counter += len(right) - j
                i += 1
            else:
                result.append(right[j])  
                j += 1 
        
        result.extend(left[i:])        
        result.extend(right[j:]) 

        outcome = result, counter
        print(f"    {outcome}")
        return outcome 

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
        instance = SolutionClass(list(case.arr))
        result = instance.count_anti_inversions()
        return result == case.expected
    
    test_solution(Solution, TEST_CASES, run_case_logic)
