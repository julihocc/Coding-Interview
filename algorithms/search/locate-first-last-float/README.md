# Locate the First and Last Position of a Float in a Sorted Array

## Problem Description

You are given a sorted array of floats (e.g., `[3.14, 3.14, 6.28, 9.42]`). Your task is to find the start and end coordinates (indices) where a target float appears in the list. If the target is not found, return `[-1, -1]`.

Example 1:
Input: `nums = [3.14, 3.14, 6.28, 9.42]`, `target = 3.14`
Output: `[0, 1]`

Example 2:
Input: `nums = [1.5, 2.5, 2.5, 2.5, 3.5]`, `target = 2.5`
Output: `[1, 3]`

Example 3:
Input: `nums = [1.1, 2.2]`, `target = 3.3`
Output: `[-1, -1]`

## Example Application
In scientific computing or financial analysis, datasets often consist of high-precision floating-point numbers sorted by value (e.g., timestamps or sensor readings). Finding the range of indices for a specific value is crucial for extracting relevant data slices efficiently.

## Approaches

### Naive Approach
Scan the array from left to right. Keep track of the first index where the target appears and the last index where it appears. This takes $O(n)$ time.

### Optimized Approach
Use binary search methods to find the first and last occurrences of the target. This reduces the time complexity to $O(\log n)$, which is significantly faster for large datasets.
