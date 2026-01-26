# Search Insert Position (Left)

## Problem Description

Given a sorted array of integers `nums`, which may contain duplicates, and a target value `target`, write a function to find the insert position.

- If `target` is found, return the index of its **leftmost** occurrence.
- If `target` is not found, return the index where it would be if it were inserted in order.

You must write an algorithm with $O(\log n)$ runtime complexity.

### Example 1

```
Input: nums = [1, 2, 3, 3, 5], target = 3
Output: 2
```

### Example 2

```
Input: nums = [1, 2, 3, 3, 5], target = 4
Output: 4
```

### Example 3

```
Input: nums = [1, 3, 5, 7, 9], target = 10
Output: 5
```

## Constraints

- $1 \le nums.length \le 10^4$
- $-10^4 \le nums[i] \le 10^4$
- $nums$ contains values sorted in ascending order.
- $-10^4 \le target \le 10^4$
