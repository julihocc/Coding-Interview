# Identify the K-th Smallest Element in a Binary Search Tree

## Problem Statement

Imagine needing to identify the player with the k-th best result while constructing a leaderboard for a game. We're expected to find this kth smallest element in a Binary Search Tree (BST) where the players' scores are stored for efficient retrieval.

Write a function that returns the `k`-th smallest element (1-indexed) in a Binary Search Tree.

### Example 1

```python
Input: root = [3, 1, 4, None, 2], k = 1
Output: 1
Explanation: The minimum element in the tree is 1.
```

### Example 2

```python
Input: root = [5, 3, 6, 2, 4, None, None, 1], k = 3
Output: 3
Explanation: The 3rd smallest element ordered ascending is 3.
```

### Constraints

* The number of nodes in the tree is $n$.
* `1 <= k <= n <= 10^4`
* `0 <= Node.val <= 10^4`

## Function Signature

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        pass
```
