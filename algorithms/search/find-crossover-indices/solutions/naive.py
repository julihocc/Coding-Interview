def findCrossoverIndex(x, y):
    """
    Naive implementation of finding the crossover index.
    Arguments:
        x: sorted list of numbers
        y: sorted list of numbers
    Returns:
        Index i such that x[i] >= y[i] and x[i+1] < y[i+1]
        (or the last index i where x[i] >= y[i])
    """
    assert len(x) == len(y)
    n = len(x)
    
    # Iterate to find the crossover point
    # We are looking for the largest index i such that x[i] >= y[i]
    for i in range(n - 1, -1, -1):
        if x[i] >= y[i]:
            return i
            
    return -1
