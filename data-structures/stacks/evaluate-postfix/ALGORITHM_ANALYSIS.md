# Algorithm Analysis: Evaluate Reverse Polish Notation

## Stack-Based Approach

The standard algorithm for evaluating Postfix expressions (Reverse Polish Notation) uses a **Stack**.

### Algorithm Steps

1.  Initialize an empty stack.
2.  Iterate through the `tokens` list.
3.  For each token:
    *   If the token is an **operand** (a number), convert it to an integer and **push** it onto the stack.
    *   If the token is an **operator** (`+`, `-`, `*`, `/`):
        *   **Pop** the top two elements from the stack. Let the first popped element be `b` and the second popped element be `a`.
        *   Perform the operation `a operator b`.
        *   **Push** the result back onto the stack.
4.  After iterating through all tokens, the stack will contain exactly one element, which is the final result.

### Careful with Division

The problem specifies "division between two integers should truncate toward zero".
In Python, the `//` operator performs **floor division** (rounds towards negative infinity).
-   `6 // -132` results in `-1`.
-   `int(6 / -132)` results in `0`.

Therefore, we must use `int(a / b)` to correctly implement truncation toward zero for negative results.

### Complexity Analysis

-   **Time Complexity**: **O(n)**, where *n* is the number of tokens. We traverse the list of tokens once. All stack operations (push, pop) and arithmetic operations are O(1).
-   **Space Complexity**: **O(n)**. In the worst case, the stack might hold a large portion of the operands before any operator is encountered (e.g., `1 2 3 4 5 + + + +`).
