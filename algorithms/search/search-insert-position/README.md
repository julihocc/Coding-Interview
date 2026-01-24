# Find or Define Insert Position in a Sorted List

## Problem Description

Our task is to find or determine the index where a target should be inserted in a sorted integer list. If the target is found, return the index. If not, return the index where it would be if it were inserted in order.

Example 1:
Input: `nums = [1,3,5,6]`, `target = 5`
Output: `2`

Example 2:
Input: `nums = [1,3,5,6]`, `target = 2`
Output: `1`

Example 3:
Input: `nums = [1,3,5,6]`, `target = 7`
Output: `4`

## Example Application
To give this problem real-world relevance, picture a document management system where reports are sorted based on their IDs. Suppose a new report comes in, and it has to be placed in the correct position based on its ID. Here, our task mirrors the system's behavior - placing a number correctly in a sorted list.

## Approaches

### Naive Approach
A basic solution might involve a left-to-right scan of the array, comparing each element with the target until we encounter an element that matches the target (where we return the index), or one that's larger (where we return the current index as that's the insertion point of our target). This approach results in a linear time complexity of $O(n)$, which is undesirable for very large arrays.

### Optimized Approach
Since the array is sorted, this is a classic binary search problem. We can find the position in $O(\log n)$ time.
- If the target is found, we return the index.
- If the target is not found, the binary search loop will terminate with `left` pointing to the correct insertion index.
