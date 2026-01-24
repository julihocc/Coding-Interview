from typing import List


def search_insert(nums: List[int], target: int) -> int:
    """
    Finds the insert position of a target element in a sorted array using binary search.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return left
