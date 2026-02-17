# Algorithm Analysis: Interleave Two Queues

This document analyzes approaches for interleaving two queues into a new queue without modifying the originals.

## Problem Statement
Given two queues $Q1$ and $Q2$ of equal size $N$, create a new queue $Q_{new}$ such that elements are interleaved: $Q1[0], Q2[0], Q1[1], Q2[1], \dots$

## Approaches

### 1. Naive Approach (List Conversion)

Convert both queues to lists (or arrays), iterate through them by index, and append elements to a new queue.

-   **Algorithm**:
    1.  Convert $Q1 \rightarrow L1$, $Q2 \rightarrow L2$.
    2.  Create empty $Q_{new}$.
    3.  Loop $i$ from $0$ to $N-1$:
        -   $Q_{new}$.append($L1[i]$)
        -   $Q_{new}$.append($L2[i]$)
-   **Complexity**:
    -   **Time**: $O(N)$ for conversion and iteration.
    -   **Space**: $O(N)$ for intermediate lists + $O(N)$ for result. Total $O(N)$.
    -   **Pros**: Easy to implement using random access.
    -   **Cons**: Creates unnecessary intermediate lists.

### 2. Optimized Approach (Direct Iteration)

Since we cannot modify original queues, we can iterate over them. In Python, `deque` supports iteration without popping. If stricter queue interface rules applied (only `peek`/`dequeue`), we would need to copy them first, but typically iteration is allowed for "read-only" access in Python.

If we strictly follow "Queue" interface where we can only `dequeue`:
We would need to Make Copies of $Q1$ and $Q2$ ($O(N)$), then destructively `dequeue` from the copies into $Q_{new}$.

-   **Algorithm (Pythonic)**:
    1.  Create empty $Q_{new}$.
    2.  Zip iterate over $Q1$ and $Q2$.
    3.  For each pair $(e1, e2)$:
        -   $Q_{new}$.append($e1$)
        -   $Q_{new}$.append($e2$)
-   **Complexity**:
    -   **Time**: $O(N)$.
    -   **Space**: $O(N)$ for the result. No extra intermediate storage.
    -   **Pros**: Efficient and clean.

## Conclusion
The optimized approach avoids creating intermediate list structures, processing elements directly into the result queue.
