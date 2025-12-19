def rotLeft(a, d):
    """
    Naive implementation of left rotation.
    Rotates the array one element at a time, d times.
    Time Complexity: O(n * d)
    """
    n = len(a)
    if n == 0:
        return a
    
    # Perform rotation d times
    for _ in range(d):
        # Rotate left by 1
        first = a[0]
        for i in range(n - 1):
            a[i] = a[i+1]
        a[n-1] = first
        
    return a
