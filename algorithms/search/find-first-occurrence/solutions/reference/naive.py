from typing import List

def find_first_occurrence(nums: List[int], target: int) -> int:
    """
    Naive implementation: Linear Scan.
    Iterate through the array and return the first index where matches target.
    Time Complexity: O(n)
    """
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
