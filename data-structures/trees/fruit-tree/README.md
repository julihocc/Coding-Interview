# Fruit Tree — Insert Node and Pre-Order Traversal

## Problem Description

You are given the **initial** fruit tree (as defined in the lesson starter code). Your task is to:

1. **Find** the `"Pear"` node using DFS search.
2. **Add** a new `"Plum"` node as a child of `"Pear"`.
3. **Return** a pre-order (DFS) traversal of the updated tree — this is the equivalent of implementing the lesson's `print_tree` function.

### Initial Tree

```
Apple
├── Banana
│   ├── Date
│   └── Elderberry
└── Cherry
    ├── Pear
    └── Grape
```

### Expected Tree After Inserting Plum

```
Apple
├── Banana
│   ├── Date
│   └── Elderberry
└── Cherry
    ├── Pear
    │   └── Plum
    └── Grape
```

### Expected Pre-Order Output

```
["Apple", "Banana", "Date", "Elderberry", "Cherry", "Pear", "Plum", "Grape"]
```

## Constraints

- Use only `add_child` to insert the new node.
- Node values are unique strings.
- The input root is always the initial fruit tree described above.

## Node Definition

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [c for c in self.children if c is not child_node]
```

## Function Signature

```python
class Solution:
    def insert_and_traverse(self, root) -> list[str]:
        # 1. Find "Pear" using DFS
        # 2. Add TreeNode("Plum") as its child
        # 3. Return pre-order traversal of the updated tree
        pass
```
