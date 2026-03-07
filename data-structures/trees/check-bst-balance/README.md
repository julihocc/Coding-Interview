# Checking the Balance of a Binary Search Tree

## Problem Statement

Write a function that checks if a Binary Search Tree (BST) is balanced. A tree is balanced if, for each vertex, the size of the left subtree differs from the size of the right subtree by at most 1.

### Example 1

```python
Input: root = [3, 9, 20, None, None, 15, 7]
Output: True
Explanation: The height difference between the left and right subtrees of every node is at most 1.
```

### Example 2

```python
Input: root = [1, 2, 2, 3, 3, None, None, 4, 4]
Output: False
Explanation: The height of the left subtree of node 1 is 3, while the height of its right subtree is 1. The difference is 2, which is strictly greater than 1.
```

### Constraints

* The number of nodes in the tree is in the range `[0, 5000]`.
* `-10^4 <= Node.val <= 10^4`

## Function Signature

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_balanced(self, root: TreeNode) -> bool:
        pass
```
