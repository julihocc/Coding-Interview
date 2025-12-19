def target_index_search(nums, target):
    """
    Naive implementation using linear search.
    Time Complexity: O(n)
    """
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
