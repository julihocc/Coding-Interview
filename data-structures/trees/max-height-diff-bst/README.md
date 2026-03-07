# Maximum Subtree Height Difference in a BST

## Problem Statement

Given the root of a Binary Search Tree (BST), write a function to find the maximum difference between the heights of the left and right subtrees for any node in the tree.

The height of a tree is defined as the number of edges on the longest path from the root to a leaf node. An empty tree has a height of `-1`, and a tree with a single node has a height of `0` (this convention can vary, but for this problem, we will consider the height of a leaf node to be 1 and empty to be 0 for simplicity, or we can just define the height of an empty tree as 0 and a leaf as 1. For this problem, let's use the standard definition: height of an empty tree is `0`, and the height of a leaf node is `1`).

The difference is always a non-negative number: the absolute difference `|left_height - right_height|`.

### Example 1

```text
Input:
      10
     /  \
    5    15
        /  \
      13    17

Output: 1
```

**Explanation:**

- Node 10: left height = 1, right height = 2. Difference = |1 - 2| = 1
- Node 15: left height = 1, right height = 1. Difference = |1 - 1| = 0
- Node 5: left height = 0, right height = 0. Difference = 0
- Node 13: left height = 0, right height = 0. Difference = 0
- Node 17: left height = 0, right height = 0. Difference = 0
The maximum difference is 1.

### Example 2

```text
Input:
         10
        /
       5
      /
     2

Output: 2
```

**Explanation:**

- Node 10: left height = 2, right height = 0. Difference = 2
- Node 5: left height = 1, right height = 0. Difference = 1
- Node 2: left height = 0, right height = 0. Difference = 0
The maximum difference is 2.

### Constraints

* The number of nodes in the tree is in the range `[0, 10^4]`.
- `-10^4 <= Node.val <= 10^4`

## Function Signature

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def max_height_diff(self, root: TreeNode) -> int:
        pass
```
