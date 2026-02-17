# Moving Average from Data Stream

## Problem Description

Given a stream of integers and a window size `m`, calculate the moving average of all integers in the sliding window.

This is a classic problem in financial programming and data science. While not directly related to queues in a strict FIFO sense (as it involves calculation rather than just adding/removing), it requires manipulating a queue to maintain the window.

## Naive Approach

A naive approach would involve continually updating a list with every new data point, removing the oldest data point if the window size is exceeded, and recalculating the average for every new data point by summing the list. This is computationally expensive ($O(m)$ per update).

## Efficient Approach

We can optimize this process by maintaining a running sum and a queue of the elements currently in the window.

### Algorithm

1.  Initialize a queue, a variable `total` for the sum, and store the window size `size`.
2.  When a new value `val` arrives:
    - If the queue is full (size `m`), remove the oldest element from the queue and subtract it from `total`.
    - Add the new `val` to the queue and add it to `total`.
    - Calculate the average as `total / len(queue)`.

### Complexity

-   **Time Complexity:** $O(1)$ per `calculate_moving_average` call.
-   **Space Complexity:** $O(m)$ to store the window elements.
