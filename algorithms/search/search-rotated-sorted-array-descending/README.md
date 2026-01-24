# Search in a Rotated Descending Sorted Array

## Problem Description

You are given a peculiar list of unique integers. It is sorted in a **decreasing** order and then rotated at a random pivot. Your mission is to hunt down a specific target number in this array and report its index. If the target is not found, return -1.

Example 1:
Input: `nums = [9, 8, 7, 1, 15, 12, 11]`, `target = 12`
Output: `5`
(Array was likely `[15, 12, 11, 9, 8, 7, 1]`, rotated)

Example 2:
Input: `nums = [5, 1]`, `target = 1`
Output: `1`

## Example Application
Imagine a leaderboard that is sorted by score (highest to lowest). Due to a database quirk, the leaderboard display starts from a random rank in the middle and wraps around. You want to find the rank (index) of a specific score in this jumbled view.

## Approaches

### Naive Approach
Perform a linear scan of the array. This works regardless of sorting or rotation but takes $O(n)$ time.

### Optimized Approach
We can use a modified binary search. Even though the array is rotated and descending, at least one half of the array (split by `mid`) will always be sorted in the standard descending manner.

1.  Check if `nums[mid]` is the target.
2.  Determine which side is sorted:
    *   If `nums[left] >= nums[mid]`: The **left** half is sorted (e.g., `[9, 8, 7, 1...]` where `mid` is `1`).
        *   Check if target is in this range: `nums[left] >= target > nums[mid]`.
        *   If so, search left. Otherwise, search right.
    *   Else (`nums[left] < nums[mid]`): The **right** half is sorted (the rotation pivot is on the left).
        *   Check if target is in this range: `nums[mid] > target >= nums[right]`.
        *   If so, search right. Otherwise, search left.
This approach yields $O(\log n)$ time complexity.
