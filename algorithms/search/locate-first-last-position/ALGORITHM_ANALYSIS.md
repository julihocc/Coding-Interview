# Locate First and Last Position - Algorithm Analysis

## 1. Naive Solution

### Approach

We perform a single pass through the array. We maintain two variables `first` and `last`, both initialized to `-1`.

- When we encounter the target for the first time (`first == -1`), we set `first = i`.
- Every time we encounter the target, we update `last = i`.

### Pseudocode (CLRS Style)

```text
NAIVE-SEARCH-RANGE(A, v)
1  first = -1
2  last = -1
3  n = A.length
4  for i = 1 to n
5      if A[i] == v
6          if first == -1
7              first = i
8          last = i
9  return [first, last]
```

### Complexity

- **Time**: $O(n)$
- **Space**: $O(1)$

## 2. Optimized Solution - Iterative

### Approach

We use two separate binary searches: one to find the **first occurrence** and another to find the **last occurrence**.

1. **Find First**: Standard binary search, but when `A[mid] == target`, we store `mid` as a candidate and continue searching left (`high = mid - 1`).
2. **Find Last**: Standard binary search, but when `A[mid] == target`, we store `mid` as a candidate and continue searching right (`low = mid + 1`).

### Pseudocode (CLRS Style)

```text
BINARY-SEARCH-FIRST(A, v)
1  low = 1
2  high = A.length
3  res = -1
4  while low <= high
5      mid = floor((low + high) / 2)
6      if A[mid] == v
7          res = mid
8          high = mid - 1
9      elseif A[mid] < v
10         low = mid + 1
11     else
12         high = mid - 1
13 return res

BINARY-SEARCH-LAST(A, v)
1  low = 1
2  high = A.length
3  res = -1
4  while low <= high
5      mid = floor((low + high) / 2)
6      if A[mid] == v
7          res = mid
8          low = mid + 1
9      elseif A[mid] < v
10         low = mid + 1
11     else
12         high = mid - 1
13 return res

SEARCH-RANGE(A, v)
1  first = BINARY-SEARCH-FIRST(A, v)
2  if first == -1
3      return [-1, -1]
4  last = BINARY-SEARCH-LAST(A, v)
5  return [first, last]
```

### Complexity

- **Time**: $O(\log n)$ - Two binary searches.
- **Space**: $O(1)$

## 3. Optimized Solution - Recursive

### Approach

The recursive approach follows the same logic using helper functions.

### Pseudocode (CLRS Style)

```text
FIND-FIRST-RECURSIVE(A, v, low, high)
1  if low > high return -1
2  mid = floor((low + high) / 2)
3  if A[mid] == v
4      left_res = FIND-FIRST-RECURSIVE(A, v, low, mid - 1)
5      if left_res != -1 return left_res
6      return mid
7  elseif A[mid] < v
8      return FIND-FIRST-RECURSIVE(A, v, mid + 1, high)
9  else
10     return FIND-FIRST-RECURSIVE(A, v, low, mid - 1)

FIND-LAST-RECURSIVE(A, v, low, high)
1  if low > high return -1
2  mid = floor((low + high) / 2)
3  if A[mid] == v
4      right_res = FIND-LAST-RECURSIVE(A, v, mid + 1, high)
5      if right_res != -1 return right_res
6      return mid
7  // ... similar else if logic ...
```

### Complexity

- **Time**: $O(\log n)$
- **Space**: $O(\log n)$

## 4. Comparison

| Aspect | Naive | Optimized (Iterative) | Optimized (Recursive) |
| :--- | :--- | :--- | :--- |
| **Time** | $O(n)$ | $O(\log n)$ | $O(\log n)$ |
| **Space** | $O(1)$ | $O(1)$ | $O(\log n)$ |
| **Pros** | Simple single pass. | Efficient. | Logic separation. |
| **Cons** | Slow for large N. | Code duplication (first vs last logic). | Recursion stack. |
