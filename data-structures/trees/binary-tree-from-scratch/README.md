# Binary Tree From Scratch — Build and In-Order Traverse

## Problem Description

This is a **synthesis exercise** inspired by the lesson's four TODOs. You must:

1. **Define** a `Node` class with `value`, `left`, and `right` attributes.
2. **Build** the following binary tree from scratch using your `Node` class.
3. **Implement** in-order traversal (left → root → right).
4. **Return** the node values as a list (the `print_tree` equivalent).

### The Tree to Build

```
        4
       / \
      2   6
     / \ / \
    1  3 5  7
```

This is a perfectly balanced Binary Search Tree (BST). In-order traversal
of a BST always yields values in **sorted order**.

### Expected In-Order Output

```
[1, 2, 3, 4, 5, 6, 7]
```

## Why In-Order?

- **In-order** (Left → Root → Right) on a BST produces sorted output.
- **Pre-order** (Root → Left → Right) is used to copy or serialize a tree.
- **Post-order** (Left → Right → Root) is used to delete or evaluate a tree.

## Constraints

- You must define the `Node` class yourself inside the `Solution`.
- Return values as `list[int]` — do not print them.
- The tree structure must match the diagram above exactly.

## Function Signature

```python
class Solution:
    def build_and_traverse(self) -> list[int]:
        # 1. Define Node (no arguments needed — build the fixed tree)
        # 2. Construct the tree shown above
        # 3. Implement in-order traversal
        # 4. Return the sorted list of values
        pass
```
