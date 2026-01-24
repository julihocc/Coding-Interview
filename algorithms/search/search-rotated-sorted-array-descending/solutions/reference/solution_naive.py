from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Search in a rotated sorted array (descending) using linear scan.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i in range(len(nums)):
        if nums[i] == target:
            return i
            
    return -1
