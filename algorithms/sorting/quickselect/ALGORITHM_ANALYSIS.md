# Quickselect - Algorithm Analysis

## 1. Naive Solution

### Approach

Sort the entire array and return the element at index $k$.

### Pseudocode (CLRS Style)

```text
NAIVE-SELECT(A, k)
1  SORT(A)
2  return A[k]
```

### Complexity

- **Time**: $O(N \log N)$
- **Space**: $O(N)$ or $O(\log N)$ depending on sort implementation.

## 2. Optimized Solution - Iterative

### Approach

We use the **Partition** subroutine from Quicksort.

- Pick a pivot and partition the array.
- If the pivot ends up at index $k$, we are done.
- If pivot index $> k$, we only need to look in the left part.
- If pivot index $< k$, we only need to look in the right part.
This eliminates half the work on average, leading to linear time.

### Pseudocode (CLRS Style)

```text
PARTITION(A, left, right)
1  pivot_idx = RANDOM(left, right)
2  SWAP(A[pivot_idx], A[right])
3  pivot = A[right]
4  store_idx = left
5  for i = left to right - 1
6      if A[i] < pivot
7          SWAP(A[store_idx], A[i])
8          store_idx = store_idx + 1
9  SWAP(A[store_idx], A[right])
10 return store_idx

QUICKSELECT-ITERATIVE(A, k)
1  left = 1
2  right = A.length
3  while left <= right
4      if left == right
5          return A[left]
6      pivot_idx = PARTITION(A, left, right)
7      if pivot_idx == k
8          return A[k]
9      elseif k < pivot_idx
10         right = pivot_idx - 1
11     else
12         left = pivot_idx + 1
```

### Complexity

- **Time**: $O(N)$ on average, $O(N^2)$ worst case.
- **Space**: $O(1)$

## 3. Optimized Solution - Recursive

### Approach

Standard recursive formulation.

### Pseudocode (CLRS Style)

```text
QUICKSELECT-RECURSIVE(A, k, left, right)
1  if left == right
2      return A[left]
3  pivot_idx = PARTITION(A, left, right)
4  if k == pivot_idx
5      return A[k]
6  elseif k < pivot_idx
7      return QUICKSELECT-RECURSIVE(A, k, left, pivot_idx - 1)
8  else
9      return QUICKSELECT-RECURSIVE(A, k, pivot_idx + 1, right)
```

### Complexity

- **Time**: $O(N)$ average.
- **Space**: $O(\log N)$ stack depth average.

## 4. Comparison

| Aspect | Naive | Optimized (Iterative) | Optimized (Recursive) |
| :--- | :--- | :--- | :--- |
| **Time (Avg)** | $O(N \log N)$ | $O(N)$ | $O(N)$ |
| **Space** | $O(1)$ (Heapsort) | $O(1)$ | $O(\log N)$ |
| **Pros** | Guaranteed time. | Lowest space usage. | Simple code. |
| **Cons** | Slower than linear. | Worst case $O(N^2)$. | Worst case $O(N^2)$. |
