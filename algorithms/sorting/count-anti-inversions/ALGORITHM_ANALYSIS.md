# Count Anti-Inversions - Algorithm Analysis

## Problem Definition

Given an array of integers, count all pairs $(i, j)$ where $i < j$ and $\text{arr}[i] < \text{arr}[j]$.

## 1. Naive Solution

### Approach

The naive approach uses nested loops to examine every possible pair of indices. For each pair $(i, j)$ where $i < j$, we check if $\text{arr}[i] < \text{arr}[j]$ and increment our counter if true.

### Pseudocode (CLRS Style)

```text
COUNT-ANTI-INVERSIONS-NAIVE(A)
1  count = 0
2  n = A.length
3  for i = 1 to n - 1
4      for j = i + 1 to n
5          if A[i] < A[j]
6              count = count + 1
7  return count
```

### Complexity

- **Time:** $O(n^2)$ - Two nested loops iterate through all pairs
- **Space:** $O(1)$ - Only a counter variable is needed

### Example Walkthrough

Array: `[2, 4, 1, 3, 5]`

```text
i=0, A[0]=2:
  j=1: 2 < 4 ✓ count=1
  j=2: 2 < 1 ✗
  j=3: 2 < 3 ✓ count=2
  j=4: 2 < 5 ✓ count=3

i=1, A[1]=4:
  j=2: 4 < 1 ✗
  j=3: 4 < 3 ✗
  j=4: 4 < 5 ✓ count=4

i=2, A[2]=1:
  j=3: 1 < 3 ✓ count=5
  j=4: 1 < 5 ✓ count=6

i=3, A[3]=3:
  j=4: 3 < 5 ✓ count=7

Result: 7
```

## 2. Optimized Solution - Modified Merge Sort

### Approach

We use a **modified merge sort** algorithm that counts anti-inversions while sorting the array. The key insight is that during the merge step, when we select an element from the left subarray, it forms anti-inversion pairs with all remaining elements in the right subarray (since the element from left is smaller and comes before them in the original array).

### Key Insight

When merging two sorted subarrays:
- **Left subarray:** `[a₁, a₂, ..., aₘ]` (sorted)
- **Right subarray:** `[b₁, b₂, ..., bₙ]` (sorted)

If we take `aᵢ` from left (because `aᵢ ≤ bⱼ`), then `aᵢ` forms anti-inversion pairs with all elements `bⱼ, bⱼ₊₁, ..., bₙ` in the right subarray.

Count increment: `remaining_elements_in_right = n - j`

### Pseudocode (CLRS Style)

```text
MERGE-SORT-COUNT-ANTI-INVERSIONS(A, left, right)
1  if left ≥ right
2      if left == right
3          return ([A[left]], 0)
4      else
5          return ([], 0)
6  
7  mid = ⌊(left + right) / 2⌋
8  
9  (left_sorted, left_count) = MERGE-SORT-COUNT-ANTI-INVERSIONS(A, left, mid)
10 (right_sorted, right_count) = MERGE-SORT-COUNT-ANTI-INVERSIONS(A, mid + 1, right)
11 
12 (merged, merge_count) = MERGE-AND-COUNT(left_sorted, right_sorted)
13 
14 total_count = left_count + right_count + merge_count
15 return (merged, total_count)
```

```text
MERGE-AND-COUNT(L, R)
1  merged = []
2  count = 0
3  i = 1, j = 1
4  
5  while i ≤ L.length and j ≤ R.length
6      if L[i] ≤ R[j]
7          merged.append(L[i])
8          count = count + (R.length - j + 1)  // Anti-inversions formed
9          i = i + 1
10     else
11         merged.append(R[j])
12         j = j + 1
13 
14 while i ≤ L.length
15     merged.append(L[i])
16     i = i + 1
17 
18 while j ≤ R.length
19     merged.append(R[j])
20     j = j + 1
21 
22 return (merged, count)
```

### Complexity

- **Time:** $O(n \log n)$
  - Divide step: $O(1)$
  - Conquer: 2 recursive calls on halves
  - Merge: $O(n)$
  - Recurrence: $T(n) = 2T(n/2) + O(n) = O(n \log n)$

- **Space:** $O(n)$
  - Temporary arrays during merge: $O(n)$
  - Recursion call stack: $O(\log n)$
  - Total: $O(n)$

### Example Walkthrough

Array: `[2, 4, 1, 3, 5]`

#### Step 1: Divide

```text
                [2, 4, 1, 3, 5]
                /              \
        [2, 4, 1]              [3, 5]
        /        \              /    \
    [2, 4]       [1]         [3]    [5]
    /    \
  [2]    [4]
```

#### Step 2: Merge and Count

**Merge [2] and [4]:**
- Take 2: count += 1 (2 < 4) → count = 1
- Take 4: no increment
- Result: `[2, 4]`, count = 1

**Merge [2, 4] and [1]:**
- Take 1: no increment (1 is from right)
- Take 2: no increment (no elements left in right)
- Take 4: no increment
- Result: `[1, 2, 4]`, count = 0 (cross-inversion)
- Total so far: 1 + 0 = 1

**Merge [3] and [5]:**
- Take 3: count += 1 (3 < 5) → count = 1
- Take 5: no increment
- Result: `[3, 5]`, count = 1

**Final Merge [1, 2, 4] and [3, 5]:**
- Take 1: count += 2 (1 < 3, 1 < 5) → count = 2
- Take 2: count += 2 (2 < 3, 2 < 5) → count = 4
- Take 3: no increment (from right)
- Take 4: count += 1 (4 < 5) → count = 5
- Take 5: no increment
- Result: `[1, 2, 3, 4, 5]`, cross count = 5

**Total Count:**
- Left subtree ([2,4,1]): 1
- Right subtree ([3,5]): 1
- Cross (merge): 5
- **Total: 1 + 1 + 5 = 7** ✓

## 3. Iterative Solution - Bottom-Up Merge Sort

### Approach

The iterative approach achieves the same O(n log n) complexity using a bottom-up merge sort strategy. Instead of recursively dividing the array, we start with subarrays of size 1 and iteratively merge them into larger sorted subarrays (size 2, 4, 8, ...).

### Key Advantage

Avoids recursion overhead and call stack depth, making it more memory-efficient for very large arrays while maintaining the same time complexity.

### Pseudocode (CLRS Style)

```text
ITERATIVE-MERGE-SORT-COUNT(A)
1  n = A.length
2  count = 0
3  size = 1
4  
5  while size < n
6      for start = 1 to n step (size * 2)
7          mid = min(start + size - 1, n)
8          end = min(start + size * 2 - 1, n)
9          
10         if mid < end
11             merge_count = MERGE-AND-COUNT(A, start, mid, end)
12             count = count + merge_count
13     
14     size = size * 2
15 
16 return count
```

### Complexity

- **Time:** $O(n \log n)$ - Same recurrence as recursive approach
- **Space:** $O(n)$ - Temporary arrays for merging (no recursion stack)

## Comparison

| Approach | Time Complexity | Space Complexity | Best For |
|----------|----------------|------------------|----------|
| Naive | $O(n^2)$ | $O(1)$ | Small arrays (n < 100) |
| Recursive Merge Sort | $O(n \log n)$ | $O(n + \log n)$ | General use, clean code |
| Iterative Merge Sort | $O(n \log n)$ | $O(n)$ | Large arrays, avoid stack overflow |

## Related Problems

- **Count Inversions:** Count pairs where $i < j$ and $\text{arr}[i] > \text{arr}[j]$ (opposite condition)
- **Merge Sort:** Foundation for the optimized solution
- **Kendall's Tau:** Statistical measure using inversion count
