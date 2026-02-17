# Algorithm Analysis: Queue Interleaving

This document analyzes approaches for interleaving the first half of a queue with the second half.

## Problem Statement
Given a queue of $N$ integers, interleave the first half with the second half.
Example: `[1, 2, 3, 4, 5, 6]` $\rightarrow$ `[1, 4, 2, 5, 3, 6]`

## Approaches

### 1. Naive Approach (Using Auxiliary Array/List)

The most intuitive approach is to empty the queue into a list, perform the interleaving using array indexing, and then fill the queue back up.

- **Algorithm**:
    1.  Dequeue all elements into an array `arr`.
    2.  Clear the queue.
    3.  Iterate from `0` to `N/2` and enqueue `arr[i]` then `arr[N/2 + i]`.
- **Complexity**:
    -   **Time**: $O(N)$ for dequeuing, creating list, and enqueuing.
    -   **Space**: $O(N)$ to store elements in the list.

### 2. Optimized Queue Approach

This approach adheres to the constraints of allowed queue operations (FIFO) and uses a single auxiliary queue (or stack) of size $N/2$.

-   **Algorithm**:
    1.  Push the first half of the elements into an auxiliary queue.
    2.  The original queue now contains only the second half.
    3.  While the auxiliary queue is not empty:
        -   Pop from auxiliary queue and enqueue to original queue.
        -   Dequeue from original queue (the head of the second half) and enqueue to back of original queue.
-   **Complexity**:
    -   **Time**: $O(N)$. We process each element a constant number of times.
    -   **Space**: $O(N)$ for the auxiliary queue (specifically $N/2$).

## Comparison

| Approach | Time Complexity | Space Complexity | Pros | Cons |
| :--- | :--- | :--- | :--- | :--- |
| Naive (List) | $O(N)$ | $O(N)$ | Simple to implement | Uses random access (requires list conversion) |
| Optimized (Queue) | $O(N)$ | $O(N)$ | Respects queue interface | Slightly more complex logic |

## Conclusion
Both approaches have linear time and space complexity. The optimized approach is preferred in interviews as it demonstrates ability to manipulate data structures within their interface constraints.
