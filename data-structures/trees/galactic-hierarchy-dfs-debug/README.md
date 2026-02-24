# Galactic Hierarchy DFS — Debug the Bug

## Problem Description

The code below attempts to perform a **Depth-First Search (DFS)** traversal on a galactic hierarchy tree. However, it contains a **bug** that causes infinite recursion.

Your mission: **identify and fix the bug** so that `depth_first_search()` correctly traverses the tree.

## The Buggy Code

```python
def depth_first_search(self):
    print(self.value, end=' -> ')
    for child in self.children:
        self.depth_first_search()  # 🐛 Bug is here!
```

## The Tree

```
Root
├── Left Child
│   ├── Left Grandchild
│   └── Right Grandchild
└── Right Child
```

## Expected DFS Output

```
['Root', 'Left Child', 'Left Grandchild', 'Right Grandchild', 'Right Child']
```

## Constraints

- Do **not** change the tree structure or the `add_child` method.
- Fix only the `depth_first_search` method.
- The traversal must visit nodes in DFS (pre-order) order.

## Node Definition

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_value):
        self.children.append(TreeNode(child_value))

    def depth_first_search(self):
        # Fix this method
        pass
```

## Function Signature

```python
class Solution:
    def dfs(self, root) -> list[str]:
        """Return nodes in DFS order using the fixed depth_first_search method."""
        pass
```
