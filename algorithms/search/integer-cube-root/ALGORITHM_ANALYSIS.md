# Integer Cube Root - Algorithm Analysis

## 1. Naive Solution

### Approach

We look for the largest integer $k$ such that $k^3 \le n$. The naive approach starts starting from $k=1$ and increments $k$ as long as $(k+1)^3 \le n$. When the loop terminates, $k$ is the answer.

### Pseudocode (CLRS Style)

```text
NAIVE-CUBE-ROOT(n)
1  if n == 0 return 0
2  k = 1
3  while (k + 1)^3 <= n
4      k = k + 1
5  return k
```

### Complexity

- **Time**: $O(n^{1/3})$ - We iterate up to the cube root of n.
- **Space**: $O(1)$

## 2. Optimized Solution - Iterative

### Approach

We can find $k$ using **Binary Search** over the range $[0, n]$. The function $f(x) = x^3$ is monotonically increasing for $x \ge 0$. We want to find $k$ such that $k^3 \le n < (k+1)^3$. This is equivalent to finding the "boundary" in the array $[0^3, 1^3, ..., n^3]$ relative to $n$.

### Pseudocode (CLRS Style)

```text
BINARY-SEARCH-CUBE-ROOT-ITERATIVE(n)
1  low = 0
2  high = n
3  result = 0
4  while low <= high
5      mid = floor((low + high) / 2)
6      if mid^3 <= n
7          result = mid
8          low = mid + 1
9      else
10         high = mid - 1
11 return result
```

### Complexity

- **Time**: $O(\log n)$
- **Space**: $O(1)$

## 3. Optimized Solution - Recursive

### Approach

Define a helper function that searches in $[low, high]$. We compare $mid^3$ with $n$.

- If $mid^3 > n$, the answer must be smaller, so we search left.
- If $mid^3 \le n$, $mid$ might be the answer, but we need to check if there is a larger valid solution (or simply checking if $(mid+1)^3 > n$).

### Pseudocode (CLRS Style)

```text
BINARY-SEARCH-CUBE-ROOT-RECURSIVE(n, low, high)
1  if low > high
2      return high  // high will be the floor answer
3  
4  mid = floor((low + high) / 2)
5  if mid^3 <= n
6      // Try to find a larger k
7      res = BINARY-SEARCH-CUBE-ROOT-RECURSIVE(n, mid + 1, high)
8      if res != NIL return res
9      return mid 
10 else
11     return BINARY-SEARCH-CUBE-ROOT-RECURSIVE(n, low, mid - 1)
```

(Note: The implemented Python version uses a specific check `cube(mid) <= n and cube(mid+1) > n` to return immediately, which is an optimization.)

### Complexity

- **Time**: $O(\log n)$
- **Space**: $O(\log n)$

## 4. Comparison

| Aspect | Naive | Optimized (Iterative) | Optimized (Recursive) |
| :--- | :--- | :--- | :--- |
| **Time** | $O(n^{1/3})$ | $O(\log n)$ | $O(\log n)$ |
| **Space** | $O(1)$ | $O(1)$ | $O(\log n)$ |
| **Pros** | Very simple loop. | Extremely fast for large $n$. | Divide and conquer logic. |
| **Cons** | Very slow for large $n$ (e.g., $10^9$). | Overflow for `mid^3` must be handled in typed languages. | Stack overhead. |
