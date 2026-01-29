# Algorithm Analysis: Merge Sort with Substring Comparison

## Overview

This is a variation of merge sort where the comparison operation is customized to only consider the first 3 characters of each string. This demonstrates how sorting algorithms can be adapted with custom comparison logic while maintaining the same time complexity.

## Key Concept: Custom Comparison

The core modification is in the comparison operation:

- **Standard merge sort:** Compares entire strings
- **Substring merge sort:** Compares only `s[:3]` (first 3 characters)

This change affects only the **merge operation**, not the divide-and-conquer structure.

---

## Approaches

### 1. Naive (Built-in Sort with Key Function)

**Algorithm:**

- Use Python's `sorted()` with `key=lambda s: s[:3]`
- The key function extracts the first 3 characters for comparison
- Timsort handles the actual sorting

**Time Complexity:** $O(n \log n)$

- Same as standard sorting
- Key extraction is $O(1)$ per element

**Space Complexity:** $O(n)$

- Creates a new sorted list
- Key function doesn't add significant space

**Pros:**

- Extremely simple and concise
- Leverages highly optimized Timsort
- Stable sort guaranteed

**Cons:**

- Doesn't demonstrate custom merge logic
- Less educational value

---

### 2. Recursive Merge Sort with Substring Comparison

**Algorithm:**

1. **Base case:** Arrays with 0 or 1 elements are already sorted
2. **Divide:** Split array at midpoint
3. **Conquer:** Recursively sort both halves
4. **Combine:** Merge with custom comparison: `left[i][:3] <= right[j][:3]`

**Modified Merge Operation:**

```python
# Standard comparison:
if left[i] <= right[j]:

# Substring comparison:
if left[i][:3] <= right[j][:3]:
```

**Time Complexity:** $O(n \log n)$

- Same recurrence as standard merge sort: $T(n) = 2T(n/2) + O(n)$
- Substring extraction `s[:3]` is $O(1)$ in Python (creates a view/slice)
- Comparison of 3-character strings is $O(1)$ (constant length)

**Space Complexity:** $O(n)$

- $O(n)$ for temporary merge arrays
- $O(\log n)$ for recursion stack
- Total: $O(n)$

**Pros:**

- Demonstrates custom comparison logic clearly
- Maintains merge sort's guaranteed performance
- Stable sort (preserves relative order)

**Cons:**

- More complex than using built-in sort
- Requires $O(n)$ extra space

---

### 3. Iterative Merge Sort with Substring Comparison

**Algorithm:**

1. Start with subarrays of size 1
2. Merge adjacent pairs using substring comparison
3. Double the size and repeat until entire array is sorted

**Modified Merge:**
Same as recursive version, but in bottom-up fashion.

**Time Complexity:** $O(n \log n)$

- $\log n$ passes through the array
- Each pass does $O(n)$ work with substring comparisons

**Space Complexity:** $O(n)$

- Temporary array for merging
- No recursion stack

**Pros:**

- Avoids recursion overhead
- Same custom comparison logic
- Better for very large datasets

**Cons:**

- More complex implementation
- Less intuitive than recursive approach

---

## Comparison Summary

| Approach | Time (Best) | Time (Avg) | Time (Worst) | Space | Stable | Custom Logic |
|----------|-------------|------------|--------------|-------|--------|--------------|
| Naive (key) | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes | Implicit |
| Recursive | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes | Explicit |
| Iterative | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes | Explicit |

---

## Implementation Details

### Substring Extraction

Python's slice operation `s[:3]` is efficient:

- Returns first 3 characters if string has ≥3 characters
- Returns entire string if length < 3
- Time: $O(1)$ (creates a view in Python 3)
- Space: $O(1)$ for the slice object

### Comparison Behavior

```python
"app"[:3] == "app"        # True
"apple"[:3] == "app"      # True
"application"[:3] == "app" # True
"ab"[:3] == "ab"          # True (uses full string)
```

### Stability

All implementations maintain stability:

- If two strings have the same first 3 characters, their relative order is preserved
- Example: `["apple", "application"]` stays in that order if both start with "app"

---

## When to Use This Variation

**Best for:**

- Sorting by prefix (e.g., area codes, country codes)
- Grouping similar strings by common prefix
- Performance optimization when full string comparison is expensive
- Educational purposes (demonstrates custom comparison logic)

**Not ideal for:**

- When you need exact string ordering
- When strings are very short (< 3 characters mostly)
- When the first 3 characters don't provide meaningful ordering

---

## Complexity Analysis: Why Still O(n log n)?

Even with custom comparison, the time complexity remains $O(n \log n)$ because:

1. **Divide step:** $O(1)$ - unchanged
2. **Conquer step:** $2T(n/2)$ - unchanged
3. **Combine step:** $O(n)$ - each comparison is still $O(1)$

The substring extraction `s[:3]` is $O(1)$, and comparing two 3-character strings is $O(1)$ (constant length), so the merge operation remains $O(n)$ overall.
