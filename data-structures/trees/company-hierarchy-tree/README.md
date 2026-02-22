# Company Hierarchy Tree — Restructure and Traverse

## Problem Description

You are given the **initial** company hierarchy tree (as defined in the lesson starter code). Your task is to **restructure** it to reflect two new hires, then return the **pre-order traversal** of the updated tree.

### Changes to Apply

1. Create a `"Senior Engineer"` node and add it as a child of `"VP Engineering"`.
2. Create a `"Product Manager"` node and add it as a child of `"VP Engineering"`.
3. **Move** `"Engineer"` so that it reports to `"Senior Engineer"` instead of `"VP Engineering"`.

### Initial Tree

```
CEO
├── VP Marketing
│   └── Director Marketing
├── VP Finance
└── VP Engineering
    └── Engineer
```

### Expected Tree After Restructuring

```
CEO
├── VP Marketing
│   └── Director Marketing
├── VP Finance
└── VP Engineering
    ├── Senior Engineer
    │   └── Engineer
    └── Product Manager
```

### Expected Pre-Order Output

```
["CEO", "VP Marketing", "Director Marketing", "VP Finance",
 "VP Engineering", "Senior Engineer", "Engineer", "Product Manager"]
```

## Constraints

- You may only use `add_child` and `remove_child` to modify the tree.
- Node values are unique strings.
- The input root is always the initial tree described above.

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
    def restructure_and_traverse(self, root) -> list[str]:
        # 1. Find VP Engineering and Engineer nodes
        # 2. Apply tree modifications using add_child / remove_child
        # 3. Return pre-order traversal of the resulting tree
        pass
```
