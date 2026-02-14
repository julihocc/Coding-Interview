# Algorithm Analysis

## Approach 1: Brute Force

For each day, iterate through all the subsequent days to find the first day with a lower temperature.

- **Time Complexity**: $O(N^2)$. In the worst case (e.g., strictly increasing temperatures), for each element, we might check all subsequent elements.
- **Space Complexity**: $O(1)$ (ignoring output array).

## Approach 2: Monotonic Stack

We can use a **Monotonic Increasing Stack** to solve this problem efficiently. The stack will store indices of days whose next cooler day hasn't been found yet.

1.  Initialize an array `answer` of size `N` with `-1`.
2.  Iterate through the temperatures from left to right (index `i`).
3.  While the stack is not empty and the current temperature `T[i]` is **lower** than the temperature at the index stored at the top of the stack (`T[stack.top()]`):
    - This means we found the next cooler day for the day at `stack.top()`.
    - Pop the index `prev_index` from the stack.
    - Calculate the wait days: `i - prev_index`.
    - Update `answer[prev_index]` with this value.
4.  Push the current index `i` onto the stack.

- **Time Complexity**: $O(N)$. Each element is pushed onto the stack once and popped at most once.
- **Space Complexity**: $O(N)$. In the worst case (strictly increasing temperatures), the stack can grow to size `N`.
