# Algorithm Analysis: Moving Average from Data Stream

This document analyzes approaches for calculating the moving average of a data stream.

## Problem Statement
Given a stream of integers and a window size $m$, calculate the moving average of all integers in the sliding window.

## Approaches

### 1. Naive Approach (List Re-summation)

Maintain a list of the last $m$ elements. When a new element comes in, append it. If the list size exceeds $m$, remove the first element (oldest). Then, sum the list and divide by the count.

-   **Algorithm**:
    -   Append new element.
    -   If `len > m`, `pop(0)`.
    -   `sum(list) / len(list)`.
-   **Complexity**:
    -   **Time**: $O(m)$ per `next()` call. `pop(0)` is $O(m)$ for list, and `sum` is $O(m)$.
    -   **Space**: $O(m)$ to store elements.

### 2. Optimized Approach (Sliding Window Sum)

Maintain a `queue` (deque) for the elements in the window and a separate `total` variable for the current sum.

-   **Algorithm**:
    -   When `val` arrives:
        -   If `queue` is full:
            -   `removed = queue.popleft()` ($O(1)$)
            -   `total -= removed`
        -   `queue.append(val)` ($O(1)$)
        -   `total += val`
        -   `average = total / len(queue)`
-   **Complexity**:
    -   **Time**: $O(1)$ per `next()` call.
    -   **Space**: $O(m)$ to store the queue.

## Comparison

| Approach | Time Complexity (per call) | Space Complexity | Pros | Cons |
| :--- | :--- | :--- | :--- | :--- |
| Naive (List) | $O(m)$ | $O(m)$ | Simple logic | Slow for large windows |
| Optimized (Deque) | $O(1)$ | $O(m)$ | Fast regardless of window size | Requires maintaining sum state |

## Conclusion
The optimized approach is significantly better for large window sizes or high-frequency data streams, reducing the per-operation cost from linear to constant time.
