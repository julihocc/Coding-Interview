# Find First Occurrence - Algorithm Analysis

## 1. Naive Solution

### Approach

The naive approach is a simple linear scan. We iterate through the array from the beginning (index 0) to the end. The first time we encounter an element equal to the target, we return its index. Since the array is sorted, the first match we find is guaranteed to be the first occurrence.

### Pseudocode (CLRS Style)

```text
NAIVE-FIND-FIRST(A, v)
1  for i = 1 to A.length
2      if A[i] == v
3          return i
4  return NIL
```

### Complexity

- **Time**: $O(n)$ - In the worst case (target at the end or not present), we scan the entire array.
- **Space**: $O(1)$ - Only a loop counter is stored.

## 2. Optimized Solution - Iterative

### Approach

We use a modified **Binary Search**. The standard binary search returns *any* index where the target is found. To find the *first* occurrence, when we find `A[mid] == target`, we assume there might be another instance to the left. Therefore, we record the current position as a potential answer and continue searching in the left half (`high = mid - 1`). If `A[mid] != target`, we proceed as usual.

### Pseudocode (CLRS Style)

```text
BINARY-SEARCH-FIRST-ITERATIVE(A, v)
1  low = 1
2  high = A.length
3  result = NIL
4  while low <= high
5      mid = floor((low + high) / 2)
6      if A[mid] == v
7          result = mid
8          high = mid - 1
9      elseif A[mid] < v
10         low = mid + 1
11     else
12         high = mid - 1
13 return result
```

### Complexity

- **Time**: $O(\log n)$ - The search space is halved in every iteration.
- **Space**: $O(1)$ - Uses constant extra space.

## 3. Optimized Solution - Recursive

### Approach

This follows the same divide-and-conquer logic as the iterative version. The helper function takes `low` and `high` bounds. If a match is found, we recursively call the function on the left subarray (`low` to `mid - 1`) to see if an earlier occurrence exists. If the recursive call returns a valid index, we return that; otherwise, we return the current `mid`.

### Pseudocode (CLRS Style)

```text
BINARY-SEARCH-FIRST-RECURSIVE(A, v, low, high)
1  if low > high
2      return NIL
3  mid = floor((low + high) / 2)
4  if A[mid] == v
5      // Found match, try finding an earlier one
6      left_result = BINARY-SEARCH-FIRST-RECURSIVE(A, v, low, mid - 1)
7      if left_result != NIL
8          return left_result
9      else
10         return mid
11 elseif A[mid] < v
12     return BINARY-SEARCH-FIRST-RECURSIVE(A, v, mid + 1, high)
13 else
14     return BINARY-SEARCH-FIRST-RECURSIVE(A, v, low, mid - 1)
```

### Complexity

- **Time**: $O(\log n)$
- **Space**: $O(\log n)$ - Due to the recursion stack depth.

## 4. Comparison

| Aspect | Naive | Optimized (Iterative) | Optimized (Recursive) |
| :--- | :--- | :--- | :--- |
| **Time** | $O(n)$ | $O(\log n)$ | $O(\log n)$ |
| **Space** | $O(1)$ | $O(1)$ | $O(\log n)$ |
| **Pros** | Simple implementation. Works on unsorted arrays too. | Most efficient in time and space. | Expresses the divide-and-conquer nature clearly. |
| **Cons** | Inefficient for large datasets. | Slightly more complex logic to handle the "first" constraint. | Recursion overhead and potential stack overflow for very large $N$. |
