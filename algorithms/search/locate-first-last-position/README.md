# Locate the First and Last Position of an Element in a Sorted Array

## Problem Description

In this problem, you are tasked with finding both the first and last positions of a certain target value in a sorted array. If the target is not found within the array, your function should return `[-1, -1]`.

Example:
Input: `nums = [5,7,7,8,8,10]`, `target = 8`
Output: `[3,4]`

Input: `nums = [5,7,7,8,8,10]`, `target = 6`
Output: `[-1,-1]`

## Example Application
To make this problem more relatable, picture a situation involving time-series analysis. For instance, you have a sorted array filled with timestamps of user activities. A user could perform the same activity multiple times, and your task is to determine the first and last instance that a particular activity was performed.

## Approaches

### Naive Approach
An immediate solution could involve scanning the entire array while taking note of the first and last appearances of the target. Although this method is sound and would yield the correct result, it is far from efficient. This linear search approach could result in a worst-case time complexity of $O(n)$.

### Optimized Approach
Since the array is sorted, we can use binary search to locate the first and last occurrences of the target. We can write two binary search functions: one to find the first occurrence and another to find the last occurrence. This approach significantly improves efficiency, reducing the time complexity to $O(\log n)$.
