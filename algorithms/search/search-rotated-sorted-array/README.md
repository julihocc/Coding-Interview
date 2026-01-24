# Search in a Rotated Sorted Array

## Problem Description

Imagine a sorted array of integers that has been rotated at an unknown pivot point. This list maintains its sorted order but now starts from a random position. Your task is to find a specific target value within this array and return its index. If the target isn't present, return -1.

For example, the initial sorted array could be `[1, 2, 4, 5, 8, 9, 11, 15]`, but after a single rotation it'd become `[8, 9, 11, 15, 1, 2, 4, 5]`.

### Example Application

Picture a server system where processes are listed in ascending order based on their IDs. Suppose a disruption rotates this list. Now, the system needs to find a process using a specific ID. A standard binary search isn't sufficient as the list, though sorted, starts at an arbitrary point.

## Approaches

### Naive Approach

A straightforward solution involves scanning each element in the array until we find a match or exhaust the list. This linear search approach is simple but computationally expensive for large lists - its time complexity is $O(n)$.

### Optimized Approach

We can modify the binary search algorithm to handle the rotation. The key observation is that for any mid element, one half of the array (either left or right) will always be sorted. We can use this property to discard half of the array in each step, achieving a time complexity of $O(\log n)$.
