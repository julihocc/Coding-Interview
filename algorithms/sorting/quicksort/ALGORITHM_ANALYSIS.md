# Quicksort - Algorithm Analysis

## 1. Naive Solution

### Approach

Not applicable in the same sense (Basic Sort *is* the problem). A "naive" implementation might check all permutations ($O(N!)$) or use a simple $O(N^2)$ sort like Bubble Sort. We will assume Bubble Sort for comparison.

### Pseudocode (CLRS Style)

```text
BUBBLE-SORT(A)
1  n = A.length
2  for i = 1 to n
3      for j = n downto i + 1
4          if A[j] < A[j-1]
5              SWAP(A[j], A[j-1])
```

### Complexity

- **Time**: $O(N^2)$
- **Space**: $O(1)$

## 2. Optimized Solution - Recursive (Standard Quicksort)

### Approach

**Divide and Conquer**:

1. Partition the array around a pivot such that elements left of pivot are smaller, and right are larger.
2. Recursively sort the left and right subarrays.

### Pseudocode (CLRS Style)

```text
PARTITION(A, p, r)
1  x = A[r]
2  i = p - 1
3  for j = p to r - 1
4      if A[j] <= x
5          i = i + 1
6          SWAP(A[i], A[j])
7  SWAP(A[i+1], A[r])
8  return i + 1

QUICKSORT-RECURSIVE(A, p, r)
1  if p < r
2      q = PARTITION(A, p, r)
3      QUICKSORT-RECURSIVE(A, p, q - 1)
4      QUICKSORT-RECURSIVE(A, q + 1, r)
```

### Complexity

- **Time**: $O(N \log N)$ average, $O(N^2)$ worst case.
- **Space**: $O(\log N)$ stack space.

## 3. Optimized Solution - Iterative

### Approach

We replace recursion with an explicit **Stack**. We push the boundaries $(low, high)$ of subarrays to be processed onto the stack. While the stack is not empty, pop a range, partition it, and push the resulting sub-ranges.

### Pseudocode (CLRS Style)

```text
QUICKSORT-ITERATIVE(A, low, high)
1  S = NEW-STACK()
2  PUSH(S, (low, high))
3  while S is not empty
4      (l, h) = POP(S)
5      if l < h
6          p = PARTITION(A, l, h)
7          // Push larger side first to minimize stack depth
8          PUSH(S, (l, p - 1))
9          PUSH(S, (p + 1, h))
```

### Complexity

- **Time**: $O(N \log N)$ average.
- **Space**: $O(\log N)$ for the stack (if optimized order), otherwise up to $O(N)$.

## 4. Comparison

| Aspect | Naive (Bubble) | Optimized (Recursive) | Optimized (Iterative) |
| :--- | :--- | :--- | :--- |
| **Time (Avg)** | $O(N^2)$ | $O(N \log N)$ | $O(N \log N)$ |
| **Space** | $O(1)$ | $O(\log N)$ | $O(\log N)$ |
| **Pros** | Simple code, stable. | Fast, in-place, cache friendly. | Avoids stack overflow. |
| **Cons** | Very slow. | Recursion depth limit. | Explicit stack is complex. |
