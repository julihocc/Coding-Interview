# Quicksort Descending - Algorithm Analysis

## 1. Problem Overview

The goal is to sort an array of integers in descending order. This is identical in complexity to standard ascending sort, merely swapping the comparison operator.

## 2. Optimized Solution - Recursive

### Approach

**Divide and Conquer**:

1. Partition the array around a pivot such that elements left of pivot are *larger* (or equal), and right are *smaller*.
2. Recursively sort the left and right subarrays.

### Complexity

- **Time**: $O(N \log N)$ average, $O(N^2)$ worst case.
- **Space**: $O(\log N)$ stack space.

## 3. Comparison

| Aspect | Ascending Quicksort | Descending Quicksort |
| :--- | :--- | :--- |
| **Constraint** | Left $\le$ Pivot < Right | Left $\ge$ Pivot > Right |
| **Logic** | `nums[j] <= pivot` | `nums[j] >= pivot` |
