# Search Insert Position - Algorithm Analysis

## 1. Naive Solution

### Approach

We iterate through the sorted array. The first element that is greater than or equal to the target is the correct insert position. If we reach the end of the array without finding such an element, the insert position is at the end (index `n`).

### Pseudocode (CLRS Style)

```text
NAIVE-SEARCH-INSERT(A, v)
1  n = A.length
2  for i = 1 to n
3      if A[i] >= v
4          return i
5  return n + 1
```

### Complexity

- **Time**: $O(n)$
- **Space**: $O(1)$

## 2. Optimized Solution - Iterative

### Approach

We use **Binary Search**. We want to find the first index `i` such that `A[i] >= target`.

- If `A[mid] == target`, we return `mid`.
- If `A[mid] < target`, the insert position must be to the right (`low = mid + 1`).
- If `A[mid] > target`, the insert position is at `mid` or to the left (`right = mid - 1`).

When the loop terminates (`low > right`), `low` will be the correct insert position.

### Pseudocode (CLRS Style)

```text
BINARY-SEARCH-INSERT-ITERATIVE(A, v)
1  low = 1
2  high = A.length
3  while low <= high
4      mid = floor((low + high) / 2)
5      if A[mid] == v
6          return mid
7      elseif A[mid] < v
8          low = mid + 1
9      else
10         high = mid - 1
11 return low
```

### Complexity

- **Time**: $O(\log n)$
- **Space**: $O(1)$

## 3. Optimized Solution - Recursive

### Approach

Recursive binary search logic.

### Pseudocode (CLRS Style)

```text
BINARY-SEARCH-INSERT-RECURSIVE(A, v, low, high)
1  if low > high
2      return low
3  mid = floor((low + high) / 2)
4  if A[mid] == v
5      return mid
6  elseif A[mid] < v
7      return BINARY-SEARCH-INSERT-RECURSIVE(A, v, mid + 1, high)
8  else
9      return BINARY-SEARCH-INSERT-RECURSIVE(A, v, low, mid - 1)
```

### Complexity

- **Time**: $O(\log n)$
- **Space**: $O(\log n)$

## 4. Comparison

| Aspect | Naive | Optimized (Iterative) | Optimized (Recursive) |
| :--- | :--- | :--- | :--- |
| **Time** | $O(n)$ | $O(\log n)$ | $O(\log n)$ |
| **Space** | $O(1)$ | $O(1)$ | $O(\log n)$ |
| **Pros** | Simple condition. | Standard efficient search. | Clean logic. |
| **Cons** | Slow. | Off-by-one errors common. | Stack usage. |
