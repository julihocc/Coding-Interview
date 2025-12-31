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
    Helper: merge two sorted lists into one sorted list.
    
    Time Complexity: O(m + n) where m = len(lst1), n = len(lst2)
    """
    # TODO: Implement two-way merge using two pointers
    pass


def oneStepKWayMerge(list_of_lists):
    """
    Helper: perform one pass of pairwise merging.
    Merge lists at indices (0,1), (2,3), etc.
    Handle odd-length lists by keeping the last unmerged.
    """
    # TODO: Implement one pass of pairwise merges
    pass


def kWayMerge(list_of_lists):
    """
    Merge k sorted lists using pairwise merging recursively.
    
    APPROACH:
    [Describe your divide-and-conquer strategy]
    
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    
    # STEP 1: Input validation
    if not list_of_lists:
        return []
    
    # STEP 2: Handle edge cases
    if len(list_of_lists) == 1:
        return list_of_lists[0]
    
    # STEP 3: Recursively merge
    # TODO: Use helper functions to merge and recurse
    pass
