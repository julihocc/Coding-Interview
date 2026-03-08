# K-th Largest Element in a BST

## Problem Statement

Given the `root` of a Binary Search Tree (BST) and an integer `k`, write a function to return the `k`-th largest element's value.
(1-indexed, meaning `k = 1` refers to the largest element, `k = 2` is the second-largest, and so on.)

A Binary Search Tree has the property that for any node `n`:

- All elements in `n`'s left subtree are strictly less than `n.val`.
- All elements in `n`'s right subtree are strictly greater than `n.val`.

### Example 1

```text
Input: k = 1
        50
       /  \
      20   60
     / \   / \
    10 30 55 70
       / \   / \
      25 35 65 80

Output: 80
```

**Explanation:** The largest element is 80 (the right-most leaf).

### Example 2

```text
Input: k = 5
        50
       /  \
      20   60
     / \   / \
    10 30 55 70
       / \   / \
      25 35 65 80

Output: 55
```

**Explanation:** The elements in sorted descending order are `[80, 70, 65, 60, 55, 50, ...]`. The 5th largest is 55.

### Constraints

* The number of nodes in the tree is $n$.
- $1 \le k \le n \le 10^4$
- $0 \le Node.val \le 10^4$

## Function Signature

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kth_largest(self, root: TreeNode, k: int) -> int:
        pass
```
