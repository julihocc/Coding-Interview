# Company Hierarchy DFS Traversal

## Problem Description

You are given the **root** of a company's organizational hierarchy tree, where each node represents a department or team. Each node may have any number of child nodes.

Implement **Depth-First Search (DFS)** on this tree to return the names of all departments in the order they are **first visited** (pre-order DFS: visit a node before its children).

DFS explores **as deep as possible** down each branch before backtracking to explore sibling branches.

## Company Hierarchy (from the lesson)

```
Head Office
├── Marketing
│   ├── SEO
│   └── Content
├── Sales
│   ├── Domestic
│   └── International
└── R&D
```

**Expected DFS Output:**

```
['Head Office', 'Marketing', 'SEO', 'Content', 'Sales', 'Domestic', 'International', 'R&D']
```

## Additional Examples

**Example 2:** Single node (no children)

```
Input: root = Node('CEO')
Output: ['CEO']
```

**Example 3:** Linear chain

```
Head Office → Sales → Domestic
Output: ['Head Office', 'Sales', 'Domestic']
```

## Constraints

- The number of nodes is in the range `[1, 100]`.
- Node values are unique, non-empty strings.
- A node may have any number of children (including zero).
- Each node is visited **exactly once** (use a `visited` set).

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
    def dfs(self, root) -> list[str]:
        """Return department names in DFS (pre-order) traversal order."""
        pass
```
