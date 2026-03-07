# Algorithm Analysis: Check BST Balance

## Exploring the Problem

The core of this problem is determining the maximum depth properties of subtrees iteratively or recursively.

A binary tree is considered balanced when the left and right sides are equal, or at least the difference is no more than one.

### 1. Naive Approach (Top-Down Recursion)

The naive approach is resolving the problem step by step: calculate the total heights of all subtrees, and then check whether the heights of each node's left and right subtrees differ by no more than one.

- **Time Complexity**: $O(n^2)$ - In the worst case (a highly unbalanced, skewed tree), determining the height of subtrees happens repeatedly for all nodes, giving a quadratic complexity bound.
- **Space Complexity**: $O(n)$ - Space used by the call stack for recursion in the worst case.

### 2. Optimized Approach (Bottom-Up Recursion)

Instead of traversing the tree multiple times, we can use recursion to do it all in one sweep. We calculate the heights of the subtrees while simultaneously checking the balance condition bottom-up.

- **Time Complexity**: $O(n)$ - Each node in the tree is processed exactly once to calculate height and bounds.
- **Space Complexity**: $O(n)$ - The recursion stack requires at most $O(n)$ space in a heavily skewed tree configuration. In a balanced tree, it will be $O(\log n)$.
