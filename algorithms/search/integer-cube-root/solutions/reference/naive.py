def integerCubeRoot(n):
    """
    Naive implementation of Integer Cube Root.
    Finds the largest integer k such that k^3 <= n using linear search.
    """
    if n == 0:
        return 0
    if n < 0:
        return -integerCubeRoot(-n) # Handle negative if needed, though problem implies positive usually
        
    k = 1
    while (k + 1) ** 3 <= n:
        k += 1
    return k
