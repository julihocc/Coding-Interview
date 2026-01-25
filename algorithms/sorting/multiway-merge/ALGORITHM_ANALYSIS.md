# Multiway Merge - Algorithm Analysis

## 1. Naive Solution

### Approach

The simplest approach is to collect all elements from the $k$ lists into a single large array and then sort it.

### Pseudocode (CLRS Style)

```text
NAIVE-MERGE(lists)
1  result = []
2  for each list L in lists
3      for each element x in L
4          APPEND(result, x)
5  SORT(result)
6  return result
```

### Complexity

- **Time**: $O(N \log N)$ where $N$ is the total number of elements.
- **Space**: $O(N)$ to store the result.

## 2. Optimized Solution - Iterative (Min-Heap)

### Approach

We use a **Min-Heap** to efficiently select the smallest available element among the $k$ sorted lists.

1. Insert the first element of each of the $k$ lists into a Min-Heap.
2. Extract the minimum element from the heap and add it to the result.
3. If the extracted element came from list $i$, insert the next element from list $i$ into the heap.
4. Repeat until the heap is empty.

### Pseudocode (CLRS Style)

```text
HEAP-MERGE-ITERATIVE(lists)
1  H = BUILD-MIN-HEAP()
2  result = []
3  k = lists.length
4
5  // Initialize heap with first element of each list
6  for i = 1 to k
7      if lists[i] is not empty
8          val = lists[i][1] // 1-based index
9          INSERT(H, (val, i, 1)) // Store val, list_index, and element_index
10
11 while H is not empty
12     (min_val, list_idx, elem_idx) = EXTRACT-MIN(H)
13     APPEND(result, min_val)
14     
15     // Push next element from the same list
16     if elem_idx < lists[list_idx].length
17         next_val = lists[list_idx][elem_idx + 1]
18         INSERT(H, (next_val, list_idx, elem_idx + 1))
19 return result
```

### Complexity

- **Time**: $O(N \log k)$ - Each element is pushed and popped once. Heap operations take $O(\log k)$.
- **Space**: $O(k)$ - Heap stores at most $k$ elements (excluding result).

## 3. Optimized Solution - Recursive (Divide & Conquer)

### Approach

We pair up the $k$ lists and merge each pair using the standard 2-way merge. This reduces the number of lists by half. We repeat this process recursively until only one list remains. This is conceptually similar to Merge Sort's "merge" phase.

### Pseudocode (CLRS Style)

```text
MERGE-TWO(L1, L2)
1  // Standard 2-way merge
2  // ... returns merged sorted list ...

DIVIDE-CONQUER-MERGE(lists)
1  k = lists.length
2  if k == 0 return []
3  if k == 1 return lists[1]
4  
5  merged_lists = []
6  for i = 1 to k step 2
7      if i + 1 <= k
8          L = MERGE-TWO(lists[i], lists[i+1])
9          APPEND(merged_lists, L)
10     else
11         APPEND(merged_lists, lists[i])
12
13 return DIVIDE-CONQUER-MERGE(merged_lists)
```

### Complexity

- **Time**: $O(N \log k)$ - In each level of recursion, we iterate over all $N$ elements. There are $\log k$ levels.
- **Space**: $O(N)$ or $O(\log k)$ depending on whether we allocate new lists or merge in-place (usually new lists in functional style).

## 4. Comparison

| Aspect | Naive | Optimized (Iterative Heap) | Optimized (Recursive D&C) |
| :--- | :--- | :--- | :--- |
| **Time** | $O(N \log N)$ | $O(N \log k)$ | $O(N \log k)$ |
| **Space** | $O(N)$ | $O(k)$ | $O(N)$ (typically) |
| **Pros** | Trivial 3-liner. | Memory efficient ($O(k)$). Streaming capable. | Easy to parallelize pairs. |
| **Cons** | Slowest ($k \ll N$). | Random access pattern not cache friendly. | High allocation overhead. |
