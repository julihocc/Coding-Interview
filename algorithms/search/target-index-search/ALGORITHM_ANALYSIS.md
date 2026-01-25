# Target Index Search - Algorithm Analysis

## 1. Naive Solution

### Approach

Scan the array. If `A[i] == target`, return `i`. If we reach the end, return `-1`.

### Pseudocode (CLRS Style)

```text
NAIVE-SEARCH(A, v)
1  n = A.length
2  for i = 1 to n
3      if A[i] == v
4          return i
5  return NIL
```

### Complexity

- **Time**: $O(n)$
- **Space**: $O(1)$

## 2. Optimized Solution - Iterative

### Approach

Standard Binary Search on a sorted array. This is the canonical example.

### Pseudocode (CLRS Style)

```text
BINARY-SEARCH-ITERATIVE(A, v)
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
11 return NIL
```

### Complexity

- **Time**: $O(\log n)$
- **Space**: $O(1)$

## 3. Optimized Solution - Recursive

### Approach

Canonical recursive binary search.

### Pseudocode (CLRS Style)

```text
BINARY-SEARCH-RECURSIVE(A, v, low, high)
1  if low > high
2      return NIL
3  mid = floor((low + high) / 2)
4  if A[mid] == v
5      return mid
6  elseif A[mid] < v
7      return BINARY-SEARCH-RECURSIVE(A, v, mid + 1, high)
8  else
9      return BINARY-SEARCH-RECURSIVE(A, v, low, mid - 1)
```

### Complexity

- **Time**: $O(\log n)$
- **Space**: $O(\log n)$

## 4. Comparison

| Aspect | Naive | Optimized (Iterative) | Optimized (Recursive) |
| :--- | :--- | :--- | :--- |
| **Time** | $O(n)$ | $O(\log n)$ | $O(\log n)$ |
| **Space** | $O(1)$ | $O(1)$ | $O(\log n)$ |
| **Pros** | Works on unsorted arrays. | Definitive $O(\log n)$ algorithm. | Classic divide-and-conquer. |
| **Cons** | Slow for sorted data. | Only for sorted data. | Stack overhead. |
