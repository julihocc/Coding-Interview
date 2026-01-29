# Algorithm Analysis: Merge Sort

## Overview

Merge sort is a divide-and-conquer sorting algorithm that divides the input array into two halves, recursively sorts them, and then merges the two sorted halves. It was invented by John von Neumann in 1945.

## Approaches

### 1. Naive (Built-in Sort)

**Algorithm:**

- Use Python's built-in `sorted()` function
- Returns a new sorted list

**Time Complexity:** $O(n \log n)$

- Python's Timsort is optimized for real-world data

**Space Complexity:** $O(n)$

- Creates a new sorted list

**Pros:**

- Simple and concise
- Highly optimized implementation
- Stable sort

**Cons:**

- Doesn't demonstrate merge sort algorithm
- Less educational value

---

### 2. Recursive Merge Sort

**Algorithm:**

1. **Base case:** If array has 0 or 1 elements, it's already sorted
2. **Divide:** Split array into two halves at the midpoint
3. **Conquer:** Recursively sort each half
4. **Combine:** Merge the two sorted halves into a single sorted array

**Merge Operation:**

- Compare elements from both halves
- Place smaller element into result array
- Continue until all elements are merged

**Time Complexity:** $O(n \log n)$

- **Divide:** $O(1)$ to find midpoint
- **Conquer:** $2T(n/2)$ for two recursive calls
- **Combine:** $O(n)$ to merge
- Recurrence: $T(n) = 2T(n/2) + O(n) = O(n \log n)$

**Space Complexity:** $O(n)$

- $O(n)$ for temporary merge arrays
- $O(\log n)$ for recursion stack
- Total: $O(n)$

**Pros:**

- Guaranteed $O(n \log n)$ worst-case performance
- Stable sort (preserves relative order of equal elements)
- Predictable performance
- Natural recursive structure

**Cons:**

- Requires $O(n)$ extra space
- Not in-place
- Recursion overhead

---

### 3. Iterative Merge Sort

**Algorithm:**

1. Start with subarrays of size 1 (already sorted)
2. Merge adjacent pairs to create sorted subarrays of size 2
3. Merge adjacent pairs of size 2 to create size 4
4. Continue doubling size until entire array is sorted

**Time Complexity:** $O(n \log n)$

- $\log n$ passes (each doubling the subarray size)
- Each pass does $O(n)$ work to merge all subarrays

**Space Complexity:** $O(n)$

- Temporary array for merging
- No recursion stack needed

**Pros:**

- Same time complexity as recursive version
- Avoids recursion overhead and stack space
- Better for very large datasets
- Easier to optimize for cache performance

**Cons:**

- More complex implementation
- Less intuitive than recursive approach
- Still requires $O(n)$ extra space

---

## Comparison Summary

| Approach | Time (Best) | Time (Avg) | Time (Worst) | Space | Stable | In-Place |
|----------|-------------|------------|--------------|-------|--------|----------|
| Naive | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes | No |
| Recursive | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes | No |
| Iterative | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes | No |

## When to Use Merge Sort

**Best for:**

- When stable sorting is required
- When guaranteed $O(n \log n)$ performance is needed
- Sorting linked lists (can be done in $O(1)$ extra space)
- External sorting (sorting data that doesn't fit in memory)

**Not ideal for:**

- When space is limited (requires $O(n)$ extra space)
- Small arrays (insertion sort is faster)
- When in-place sorting is required (use quicksort or heapsort)

## Optimizations

1. **Hybrid approach:** Switch to insertion sort for small subarrays (typically < 10-15 elements)
2. **Natural merge sort:** Take advantage of existing sorted runs in the data
3. **In-place merge:** More complex but reduces space to $O(1)$ (though with worse constant factors)
4. **Parallel merge sort:** Divide-and-conquer structure is naturally parallelizable
