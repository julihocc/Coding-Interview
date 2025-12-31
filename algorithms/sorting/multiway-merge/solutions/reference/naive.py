def kWayMerge(list_of_lists):
    """
    Naive implementation of K-Way Merge.
    Flattens the list of lists and sorts the result.
    Complexity: O(N log N) where N is total number of elements.
    """
    combined = []
    for lst in list_of_lists:
        combined.extend(lst)
    return sorted(combined)
