# Find Crossover Indices - Algorithm Analysis

## 1. Naive Solution

### Approach

The problem asks for the largest index $i$ such that $x[i] \ge y[i]$. The naive approach scans the arrays from the last index (`n-1`) down to `0`. The first index $i$ that satisfies the condition is the answer. If no such index exists, it returns `-1`.

### Pseudocode (CLRS Style)

```text
NAIVE-FIND-CROSSOVER(x, y)
1  n = x.length
2  for i = n downto 1
3      if x[i] >= y[i]
4          return i
5  return NIL
```

### Complexity

- **Time**: $O(n)$ - Worst case scans the entire array.
- **Space**: $O(1)$ - Constant space.

## 2. Optimized Solution - Iterative

### Approach

Since the condition $x[i] \ge y[i]$ is monotonic (it is true for a prefix of indices and then becomes false), we can use binary search. We are looking for the "boundary" where the condition switches from true to false. Specifically, we want the rightmost index where it is true.

- If $x[mid] \ge y[mid]$, then $mid$ is a valid candidate, but there might be a larger index to the right. So we search `[mid, high]`.
- If $x[mid] < y[mid]$, then the condition is false at $mid$ and potentially all indices to the right. So we search `[low, mid]`.

Note: Care must be taken to avoid infinite loops when `low` and `high` are adjacent.

### Pseudocode (CLRS Style)

```text
BINARY-SEARCH-CROSSOVER-ITERATIVE(x, y)
1  low = 1
2  high = x.length
3  if x.length == 0 return NIL
4  
5  while low + 1 < high
6      mid = floor((low + high) / 2)
7      if x[mid] >= y[mid]
8          low = mid    // mid is feasible, look right
9      else
10         high = mid   // mid is not feasible (or we want smaller), look left
11
12 // Check boundaries after loop
13 if x[high] >= y[high] return high
14 if x[low] >= y[low] return low
15 return NIL
```

### Complexity

- **Time**: $O(\log n)$
- **Space**: $O(1)$

## 3. Optimized Solution - Recursive

### Approach

The recursive approach directly implements the divide-and-conquer logic.

### Pseudocode (CLRS Style)

```text
BINARY-SEARCH-CROSSOVER-RECURSIVE(x, y, low, high)
1  if low == high
2      if x[low] >= y[low] return low
3      else return NIL
4  if low + 1 == high
5      if x[high] >= y[high] return high
6      if x[low] >= y[low] return low
7      return NIL
8
9  mid = floor((low + high) / 2)
10 if x[mid] >= y[mid]
11     return BINARY-SEARCH-CROSSOVER-RECURSIVE(x, y, mid, high)
12 else
13     return BINARY-SEARCH-CROSSOVER-RECURSIVE(x, y, low, mid)
```

### Complexity

- **Time**: $O(\log n)$
- **Space**: $O(\log n)$

## 4. Comparison

| Aspect | Naive | Optimized (Iterative) | Optimized (Recursive) |
| :--- | :--- | :--- | :--- |
| **Time** | $O(n)$ | $O(\log n)$ | $O(\log n)$ |
| **Space** | $O(1)$ | $O(1)$ | $O(\log n)$ |
| **Pros** | Simple, easy to verify visually. | Efficient for large inputs. | Clean logic mapping to the problem structure. |
| **Cons** | Slow for large $N$. | Boundary conditions (infinite loop) can be tricky. | Recursion depth overhead. |
