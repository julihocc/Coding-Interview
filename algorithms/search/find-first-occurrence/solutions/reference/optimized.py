from typing import List

def find_first_occurrence(nums: List[int], target: int) -> int:
    """
    Optimized implementation: Binary Search.
    Finds the first occurrence of target.
    Time Complexity: O(log n)
    """
    low, high = 0, len(nums) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            result = mid
            # Continue searching in the left half for the first occurrence
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return result
