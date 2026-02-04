# Algorithm Analysis: Are Brackets Balanced?

## 1. Stack-Based Approach

The most common and efficient way to solve this problem is using a **Stack** data structure. Steps:

1.  Initialize an empty stack.
2.  Iterate through the input string character by character.
3.  If the current character is an opening bracket (`(`, `{`, `[`), push it onto the stack.
4.  If the current character is a closing bracket (`)`, `}`, `]`), check if the stack is empty.
    *   If the stack is empty, it means there is no corresponding opening bracket, so the string is invalid. Return `False`.
    *   If the stack is not empty, pop the top element from the stack. Check if the popped element matches the corresponding opening bracket for the current closing character. If not, return `False`.
5.  After iterating through the entire string, check if the stack is empty.
    *   If it is empty, all opening brackets were properly closed. Return `True`.
    *   If it is not empty, there are some opening brackets left unmatched. Return `False`.

### Complexity Analysis

-   **Time Complexity**: **O(n)**, where *n* is the length of the string. We iterate through the string once. Operations on the stack (push and pop) are O(1).
-   **Space Complexity**: **O(n)**. In the worst case (e.g., `(((((`), we might push all characters onto the stack.

## 2. Corner Cases

-   **Empty String**: Should return `True` (an empty string is considered valid).
-   **Single Character**: Should return `False`.
-   **Only Opening/Closing Brackets**: Should return `False`.
