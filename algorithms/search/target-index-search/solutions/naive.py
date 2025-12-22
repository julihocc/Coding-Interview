from typing import List

def target_index_search(nums: List[int], target: int) -> int:
    """
    Naive implementation using linear search.
    Time Complexity: O(n)
    """
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
