from typing import List

def quickselect(nums: List[int], k: int) -> int:
    """
    Sort the array and return the k-th smallest element.
    Time: O(n log n), Space: O(n) for the sorted copy.
    """
    sorted_nums = sorted(nums)
    return sorted_nums[k]
