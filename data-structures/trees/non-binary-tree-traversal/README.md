# Non-Binary Tree Level-Order Traversal

## Problem Description

Given the `root` of a non-binary (multi-way) tree — where each node may have any number of children — return the **level-order (BFS) traversal** of its nodes' values as a list.

Level-order traversal visits nodes **level by level**, from left to right, starting from the root.

## Examples

**Example 1:** (the tree from the lesson)

```
         1
       / | \
      2  3  4
     / \    |
    5   6   7
```

```
Input: root = Node(1), with children [Node(2), Node(3), Node(4)], etc.
Output: [1, 2, 3, 4, 5, 6, 7]
```

**Example 2:** Single node

```
Input: root = Node(42)
Output: [42]
```

**Example 3:** Root with single child

```
    10
     \
      20
```

```
Input: root = Node(10), children=[Node(20)]
Output: [10, 20]
```

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-1000 <= Node.value <= 1000`
- A node may have any number of children (including zero).

## Node Definition

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
```

## Function Signature

```python
class Solution:
    def level_order(self, root) -> list[int]:
        # Your implementation here
        pass
```
