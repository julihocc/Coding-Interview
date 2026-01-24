from typing import List


def search_range(nums: List[float], target: float) -> List[int]:
    """
    Finds the first and last position of a target float in a sorted array using linear scan.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    first, last = -1, -1
    for i in range(len(nums)):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    
    return [first, last]
