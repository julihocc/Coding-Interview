def findCrossoverIndexHelper(x, y, left, right):
    # Note: Output index i such that 
    #         left <= i <= right
    #         x[i] <= y[i]
    # First, Write down our invariants as assertions here
    assert(len(x) == len(y))
    assert(left >= 0)
    assert(left <= right-1)
    assert(right < len(x))
    # Here is the key property we would like to maintain.
    # assert(x[left] > y[left]) 
    # assert(x[right] < y[right])
    
    # Base case: adjacent logic
    if left + 1 == right:
        return left

    mid = (left + right) // 2
    
    if x[mid] > y[mid]:
        return findCrossoverIndexHelper(x, y, mid, right)
    else:
        # x[mid] <= y[mid]
        # We want to maintain x[left] > y[left] and x[right] < y[right]
        # BUT here we are simplifying validation logic. 
        # Actually checking the logic:
        # If x[mid] <= y[mid], then mid behaves like the 'right' side (since y is bigger or equal).
        # Wait, the invariant for Left side is x[i] >= y[i] ? No, problem says find i such that x[i] >= y[i] and x[i+1] < y[i+1].
        # In the example: x=0, y=-2 -> x >= y.
        # x=6, y=7 -> x < y.
        # So Left Side: x >= y.
        # Right Side: x < y.
        # If x[mid] > y[mid], it satisfies Left Side. So we search [mid, right].
        # If x[mid] <= y[mid]:
        #   If x[mid] < y[mid], it satisfies Right Side. So we search [left, mid].
        #   If x[mid] == y[mid], it satisfies Left Side (x >= y). So we search [mid, right].
        
        if x[mid] >= y[mid]:
             return findCrossoverIndexHelper(x, y, mid, right)
        else:
             return findCrossoverIndexHelper(x, y, left, mid)

def findCrossoverIndex(x, y):
    assert(len(x) == len(y))
    # assert(x[0] > y[0]) # Can't always assert this if we want robust code, but problem guarantees it
    n = len(x)
    # assert(x[n-1] < y[n-1]) 
    return findCrossoverIndexHelper(x, y, 0, n-1)
