"""
TEMPLATE: Multiway Merge Solution

Function Signature:
    def kWayMerge(list_of_lists):

Problem:
    Merge k sorted lists into a single sorted list.
    Each list in list_of_lists is already sorted in ascending order.

Reference: See ../README.md for full problem description
"""


def kWayMerge(list_of_lists):
    """
    [FILL IN: Brief one-liner describing your approach]
    
    APPROACH:
    [Describe your strategy here - e.g., Flatten & Sort, Pairwise Merging, Heap]
    
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    
    # STEP 1: Input validation
    if not list_of_lists:
        return []
    
    # STEP 2: Handle edge cases
    if len(list_of_lists) == 1:
        return list_of_lists[0]
    
    # STEP 3: Initialize helper functions (if needed)
    # [Define two-way merge, partition merge steps, etc.]
    
    # STEP 4: Main merging algorithm
    # [Implement your solution here - leverage that sublists are sorted!]
    pass
    
    # STEP 5: Return merged result
    # [return merged_sorted_list]
