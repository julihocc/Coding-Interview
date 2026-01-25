# Search Rotated Sorted Array - Algorithm Analysis

## 1. Naive Solution

### Approach

A standard linear scan of the array. This works regardless of rotation or sorting.

### Pseudocode (CLRS Style)

```text
NAIVE-SEARCH(A, v)
1  n = A.length
2  for i = 1 to n
3      if A[i] == v
4          return i
5  return -1
```

### Complexity

- **Time**: $O(n)$
- **Space**: $O(1)$

## 2. Optimized Solution - Iterative

### Approach

We use **Binary Search**. In a rotated sorted array, at least one half (left or right) is always sorted. We determine which half is sorted by comparing `A[low]` and `A[mid]`.

1. If `A[low] <= A[mid]`, the **left half** `[low...mid]` is sorted.
   - We check if the target `v` lies within this sorted range: `A[low] <= v < A[mid]`.
   - If yes, search left. Otherwise, search right.
2. If `A[low] > A[mid]`, the pivot is in the left half, implying the **right half** `[mid...high]` is sorted.
   - We check if the target `v` lies within this sorted range: `A[mid] < v <= A[high]`.
   - If yes, search right. Otherwise, search left.

### Pseudocode (CLRS Style)

```text
BINARY-SEARCH-ROTATED-ITERATIVE(A, v)
1  low = 1
2  high = A.length
3  while low <= high
4      mid = floor((low + high) / 2)
5      if A[mid] == v
6          return mid
7      
8      if A[low] <= A[mid]
9          // Left half is sorted
10         if A[low] <= v and v < A[mid]
11             high = mid - 1
12         else
13             low = mid + 1
14     else
15         // Right half is sorted
16         if A[mid] < v and v <= A[high]
17             low = mid + 1
18         else
19             high = mid - 1
20 return -1
```

### Complexity

- **Time**: $O(\log n)$
- **Space**: $O(1)$

## 3. Optimized Solution - Recursive

### Approach

Recursive implementation of the logic above.

### Pseudocode (CLRS Style)

```text
BINARY-SEARCH-ROTATED-RECURSIVE(A, v, low, high)
1  if low > high
2      return -1
3  mid = floor((low + high) / 2)
4  if A[mid] == v
5      return mid
6  
7  if A[low] <= A[mid]
8      if A[low] <= v and v < A[mid]
9          return BINARY-SEARCH-ROTATED-RECURSIVE(A, v, low, mid - 1)
10     else
11         return BINARY-SEARCH-ROTATED-RECURSIVE(A, v, mid + 1, high)
12 else
13     if A[mid] < v and v <= A[high]
14         return BINARY-SEARCH-ROTATED-RECURSIVE(A, v, mid + 1, high)
15     else
16         return BINARY-SEARCH-ROTATED-RECURSIVE(A, v, low, mid - 1)
```

### Complexity

- **Time**: $O(\log n)$
- **Space**: $O(\log n)$

## 4. Comparison

| Aspect | Naive | Optimized (Iterative) | Optimized (Recursive) |
| :--- | :--- | :--- | :--- |
| **Time** | $O(n)$ | $O(\log n)$ | $O(\log n)$ |
| **Space** | $O(1)$ | $O(1)$ | $O(\log n)$ |
| **Pros** | Simple, works if multiple pivots (not fully sorted). | Efficient. | Elegant mapping of logic. |
| **Cons** | Slow. | Complex condition logic. | Stack overhead. |
