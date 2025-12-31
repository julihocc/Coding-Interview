"""TEMPLATE: Multiway Merge Solution

Function Signature:
    def kWayMerge(list_of_lists):

Problem:
    Merge k sorted lists into a single sorted list.
    Each list in list_of_lists is already sorted in ascending order.

Reference: See ../README.md for full problem description
"""


def twoWayMerge(lst1, lst2):
    """
    Helper function: merge two sorted lists into one sorted list.
    
    Time Complexity: O(m + n) where m = len(lst1), n = len(lst2)
    """
    i = 0
    j = 0
    m = len(lst1)
    n = len(lst2)
    merged = []
    
    while i < m and j < n:
        if lst1[i] <= lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    
    # Append remaining elements
    while i < m:
        merged.append(lst1[i])
        i += 1
    while j < n:
        merged.append(lst2[j])
        j += 1
    
    return merged


def oneStepKWayMerge(list_of_lists):
    """
    Helper function: perform one pass of pairwise merging.
    Merge lists at indices (0,1), (2,3), etc.
    Handles odd-length lists by keeping the last list unmerged.
    """
    if len(list_of_lists) <= 1:
        return list_of_lists
    
    ret_list_of_lists = []
    k = len(list_of_lists)
    for i in range(0, k, 2):
        if i < k - 1:
            ret_list_of_lists.append(twoWayMerge(list_of_lists[i], list_of_lists[i + 1]))
        else:
            ret_list_of_lists.append(list_of_lists[k - 1])
    
    return ret_list_of_lists


def kWayMerge(list_of_lists):
    """
    Merge k sorted lists using pairwise merging recursively.
    
    APPROACH:
    Divide and conquer: repeatedly merge pairs of lists until only one remains.
    
    Time Complexity: O(n log k) where n = total elements, k = number of lists
    Space Complexity: O(n)
    """
    
    # STEP 1: Input validation
    if not list_of_lists:
        return []
    
    # STEP 2: Handle edge cases
    if len(list_of_lists) == 1:
        return list_of_lists[0]
    
    # STEP 3: Recursively merge
    new_list_of_lists = oneStepKWayMerge(list_of_lists)
    return kWayMerge(new_list_of_lists)
