from typing import List

def target_index_search(nums: List[int], target: int) -> int:
    """
    Finds the index of a target value in a sorted array using binary search.

    Args:
        nums (List[int]): A sorted list of distinct integers.
        target (int): The integer to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = nums[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
