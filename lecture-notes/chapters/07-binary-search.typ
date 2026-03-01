= Binary Search

Binary Search is an $O(log n)$ algorithm used to find a target value within a sorted array. It is incredibly powerful because it effectively eliminates half of the remaining search space with every single comparison.

== Core Pattern

Instead of checking every element sequentially ($O(n)$ linear scan), binary search maintains two pointers, typically called `left` and `right`.
- Calculate the `middle` index between `left` and `right`.
- Compare the element at `middle` to the `target`.
- If the `target` matches, return the index.
- If the `target` is smaller, search the left half bounded by `middle - 1`.
- If the `target` is larger, search the right half bounded by `middle + 1`.

=== Typical Constraints and Edge Cases

The standard condition for the search loop is `while left <= right`. This ensures we check single-element arrays or the boundary elements if the target is at the very beginning or end.

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

== Variations

While simple to write for exact matches, binary search can be confusing when finding boundaries or dealing with duplicates.

- *First Occurrence (Lower Bound):* If `nums[mid] == target`, don't stop. Record `mid` as a potential answer and keep searching the left half (`right = mid - 1`) to see if an earlier occurrence exists.
- *Last Occurrence (Upper Bound):* Similarly, record the answer and keep searching the right half (`left = mid + 1`).
- *Binary Search on Answer Space:* Not restricted to arrays! If the condition is monotonic (e.g., if a capacity of $X$ works, $X+1$ must also work), you can binary search the mathematical range of possible answers.
