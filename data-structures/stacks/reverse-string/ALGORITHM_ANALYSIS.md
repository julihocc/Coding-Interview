# Algorithm Analysis: Reverse a String using Stack

## Stack-Based Approach

The problem requires reversing a string using a Stack. A Stack follows the **LIFO (Last-In, First-Out)** principle, which makes it naturally suitable for reversing sequences.

### Algorithm Steps

1.  **Initialize**: Create an empty stack.
2.  **Push**: Iterate through the input string `s` from beginning to end. Push each character onto the stack.
3.  **Pop**: Initialize an empty list (or string builder) for the result. Loop while the stack is not empty:
    *   Pop the top element from the stack.
    *   Append the popped element to the result list.
4.  **Join**: Join the list of characters to form the final reversed string.

### Complexity Analysis

-   **Time Complexity**: **O(n)**, where *n* is the length of the string.
    -   We iterate through the string once to push all characters: O(n).
    -   We pop all characters from the stack: O(n).
    -   Total time is O(n) + O(n) = O(2n) ≈ O(n).

-   **Space Complexity**: **O(n)**.
    -   We need a stack to store all *n* characters of the string.
    -   We also need space for the output string (which is unavoidable).

### Why use a Stack?

While string reversal can be done in-place or using two pointers (swapping elements from both ends), using a Stack explicitly demonstrates checking the LIFO property. This is often asked to test understanding of the data structure rather than finding the most memory-efficient string reversal algorithm.
