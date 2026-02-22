# Binary Tree In-Order Traversal

## Problem Description

Given the `root` of a binary tree, return the **in-order traversal** of its nodes' values as a list.

In-order traversal visits nodes in the following order:
1. Left subtree
2. Current node (root of subtree)
3. Right subtree

## Examples

**Example 1:** (the tree from the lesson)

```
        1
       / \
      2   3
     / \   \
    4   5   6
```

```
Input: root = Node(1), with left=Node(2), right=Node(3), etc.
Output: [4, 2, 5, 1, 3, 6]
```

**Example 2:** Single node

```
Input: root = Node(7)
Output: [7]
```

**Example 3:** Left-only chain

```
    3
   /
  2
 /
1
```

```
Input: root = Node(3) -> left Node(2) -> left Node(1)
Output: [1, 2, 3]
```

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-1000 <= Node.value <= 1000`

## Node Definition

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

## Function Signature

```python
class Solution:
    def in_order(self, root) -> list[int]:
        # Your implementation here
        pass
```
