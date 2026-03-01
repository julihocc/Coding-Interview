== Binary Search

Binary Search is an $O(log n)$ algorithm used to find a target value within a sorted array. It effectively eliminates half of the remaining search space with every single comparison.

=== Core Pattern

Instead of checking every element sequentially ($O(n)$ linear scan), binary search maintains two pointers, `left` and `right`.
- Calculate the `middle` index between `left` and `right`.
- Compare the element at `middle` to the `target`.
- If the `target` matches, return the index.
- If the `target` is smaller, search the left half (`right = middle - 1`).
- If the `target` is larger, search the right half (`left = middle + 1`).

The standard loop condition is `while left <= right`.

```python
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

=== Variations

- *First Occurrence (Lower Bound):* If `nums[mid] == target`, record `mid` and keep searching left (`right = mid - 1`).
- *Last Occurrence (Upper Bound):* Record `mid` and keep searching right (`left = mid + 1`).
- *Binary Search on Answer Space:* If the condition is monotonic (e.g., if capacity $X$ works, $X+1$ must also work), you can binary search the mathematical range of possible answers.
