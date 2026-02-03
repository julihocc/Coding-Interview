# Count Anti-Inversions

## Problem Statement

Given an array of integers, count the number of **anti-inversion pairs**. An anti-inversion pair is defined as a pair of indices $(i, j)$ where:
- $i < j$ (first index comes before second index)
- $\text{nums}[i] < \text{nums}[j]$ (element at first index is strictly less than element at second index)

In other words, count all pairs of elements where the earlier element is smaller than the later element.

## Constraints

- Array length: $1 \leq n \leq 10^5$
- Element values: $-10^9 \leq \text{nums}[i] \leq 10^9$
- Array can contain negative numbers, positive numbers, and duplicates
- Only strict inequalities count (not equal values)

## Examples

### Example 1

```python
arr = [2, 4, 1, 3, 5]
# Anti-inversion pairs:
# (0,1): 2 < 4 ✓
# (0,3): 2 < 3 ✓
# (0,4): 2 < 5 ✓
# (1,4): 4 < 5 ✓
# (2,3): 1 < 3 ✓
# (2,4): 1 < 5 ✓
# (3,4): 3 < 5 ✓
# Result: 7
```

### Example 2: Already Sorted

```python
arr = [1, 2, 3, 4, 5]
# All pairs are anti-inversions
# Result: 10 (which is n*(n-1)/2 = 5*4/2)
```

### Example 3: Reverse Sorted

```python
arr = [5, 4, 3, 2, 1]
# No anti-inversions (all elements decrease)
# Result: 0
```

### Example 4: All Equal

```python
arr = [3, 3, 3, 3]
# No strict inequalities
# Result: 0
```

### Example 5: Negative Numbers

```python
arr = [-3, -1, 0, 2, 5]
# All pairs are anti-inversions (sorted)
# Result: 10
```

### Example 6: Duplicates Mixed

```python
arr = [2, 2, 3, 1, 3]
# (0,2): 2 < 3 ✓
# (1,2): 2 < 3 ✓
# (1,4): 2 < 3 ✓
# (3,4): 1 < 3 ✓
# Result: 4
```

## Method Signature

```python
class Solution:
    def __init__(self, arr: List[int]):
        self.arr = arr
    
    def count_anti_inversions(self) -> int:
        """Returns the count of anti-inversion pairs."""
        pass
```

## Approaches

### Naive Solution: O(n²)

Use nested loops to check all possible pairs:
- Outer loop: iterate through each element
- Inner loop: check all elements after current element
- Count when `arr[i] < arr[j]`

**Time Complexity:** $O(n^2)$  
**Space Complexity:** $O(1)$

### Recursive Solution: O(n log n)

Use recursive merge sort:
- During merge, count anti-inversions formed between left and right subarrays
- When taking element from left array, it forms anti-inversions with all remaining elements in right array
- Recursively count in left half, right half, and during merge

**Time Complexity:** $O(n \log n)$  
**Space Complexity:** $O(n)$

### Iterative Solution: O(n log n)

Use iterative merge sort:
- Bottom-up approach merging subarrays of size 1, 2, 4, 8, ...
- Count anti-inversions during each merge operation
- Same counting logic as recursive but without recursion overhead

**Time Complexity:** $O(n \log n)$  
**Space Complexity:** $O(n)$

## Key Insights

1. **Anti-inversions vs Inversions:** Anti-inversions count ascending pairs while standard inversions count descending pairs
2. **Sorted array property:** A fully sorted array has the maximum number of anti-inversions: $\frac{n(n-1)}{2}$
3. **Reverse sorted property:** A reverse-sorted array has zero anti-inversions
4. **Merge sort connection:** The merge step naturally counts anti-inversions when merging sorted subarrays
5. **Recursive vs Iterative:** Both achieve O(n log n), but iterative avoids recursion stack overhead

## Testing

Run the judge to test your solution:

```bash
python algorithms/sorting/count-anti-inversions/judge.py
```

Test individual solutions:

```bash
python algorithms/sorting/count-anti-inversions/solutions/solution_naive.py
python algorithms/sorting/count-anti-inversions/solutions/solution_recursive.py
python algorithms/sorting/count-anti-inversions/solutions/solution_iterative.py
```
