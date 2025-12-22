# Integer Cube Root

## Problem Statement

The integer cube root of a positive number $n$ is the smallest number $i$ such that $i^3 \leq n$ but $(i+1)^3 > n$.

For instance, the integer cube root of $100$ is $4$ since $4^3 \leq 100$ but $5^3 > 100$. Likewise, the integer cube root of $1000$ is $10$.

## Invariant

The algorithm maintains the invariant:
$$\text{left}^3 < n\; \text{and}\; \text{right}^3 > n$$

This ensures that the answer lies strictly between `left` and `right`.
