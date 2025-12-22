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
    assert(x[left] > y[left])
    assert(x[right] < y[right])
    
    # Base case: adjacent logic
    if left + 1 == right:
        return left

    mid = (left + right) // 2
    
    # x[mid] > y[mid] -> mid is like left
    if x[mid] > y[mid]:
        return findCrossoverIndexHelper(x, y, mid, right)
    else:
        # x[mid] <= y[mid] -> mid is like right (but condition said x[right] < y[right])
        # Wait, the problem says find i such that x[i] >= y[i] (Wait, the example says y_i <= x_i) 
        # and y_{i+1} > x_{i+1}. 
        # But the invariants are x[left] > y[left] and x[right] < y[right].
        # In example: x=[0,2,4,5,6], y=[-2,0,2,4,7]. 
        # i=0: x=0, y=-2. x > y.
        # i=4: x=6, y=7. x < y.
        # We want i such that x[i] >= y[i] and x[i+1] < y[i+1].
        # This means we are looking for the transition from x >= y to x < y.
        # x[left] > y[left] implies left is in the ">= region".
        # x[right] < y[right] implies right is in the "< region".
        # So we want the last index where x >= y.
        
        # If x[mid] > y[mid], then mid is in the ">= region". We want to search to the right of mid, including mid.
        # So left = mid.
        
        # If x[mid] <= y[mid], (Wait, if x < y, then mid is in "< region").
        # If x[mid] == y[mid], the problem says find x_i >= y_i. So mid satisfies the left condition.
        # But wait, earlier I said "x[right] < y[right]". The invariant is strictly <.
        # If x[mid] == y[mid], then mid is a valid 'i' potentially? 
        # Or mid is part of the 'left' side?
        # The goal is x[i] >= y[i]. So if x[mid] == y[mid], it belongs to the left side property?
        # Yes.
        
        # Reformulate:
        # Left side property: x[k] >= y[k]
        # Right side property: x[k] < y[k]
        # We start with x[left] > y[left] (sits in Left property).
        # We start with x[right] < y[right] (sits in Right property).
        # We want i such that i has Left property and i+1 has Right property.
        
        # Logic:
        # mid = (left + right) // 2
        # if x[mid] > y[mid]: mid has Left property. New range [mid, right].
        # if x[mid] < y[mid]: mid has Right property. New range [left, mid].
        # if x[mid] == y[mid]: mid has Left property. New range [mid, right].
        
        # Combine: if x[mid] >= y[mid]: left = mid. Else: right = mid.
        pass

    if x[mid] >= y[mid]:
        return findCrossoverIndexHelper(x, y, mid, right)
    else:
        return findCrossoverIndexHelper(x, y, left, mid)

def findCrossoverIndex(x, y):
    assert(len(x) == len(y))
    assert(x[0] > y[0])
    n = len(x)
    assert(x[n-1] < y[n-1]) # Note: this automatically ensures n >= 2 why?
    return findCrossoverIndexHelper(x, y, 0, n-1)

if __name__ == "__main__":
    # BEGIN TEST CASES
    j1 = findCrossoverIndex([0, 1, 2, 3, 4, 5, 6, 7], [-2, 0, 4, 5, 6, 7, 8, 9])
    print('j1 = %d' % j1)
    assert j1 == 1, "Test Case # 1 Failed"

    j2 = findCrossoverIndex([0, 1, 2, 3, 4, 5, 6, 7], [-2, 0, 4, 4.2, 4.3, 4.5, 8, 9])
    print('j2 = %d' % j2)
    assert j2 == 1 or j2 == 5, "Test Case # 2 Failed"

    j3 = findCrossoverIndex([0, 1], [-10, 10])
    print('j3 = %d' % j3)
    assert j3 == 0, "Test Case # 3 failed"

    j4 = findCrossoverIndex([0,1, 2, 3], [-10, -9, -8, 5])
    print('j4 = %d' % j4)
    assert j4 == 2, "Test Case # 4 failed"

    print('Congratulations: all test cases passed - 10 points')
