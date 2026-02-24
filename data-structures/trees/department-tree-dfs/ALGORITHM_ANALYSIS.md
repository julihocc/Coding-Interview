# Algorithm Analysis: Department Tree DFS — Implement the Missing Logic

## What's Missing and Why

The starter code already handles visiting the current node:

```python
def traverse(self, visited=None):
    if visited is None:
        visited = set()
    print(self.name)
    visited.add(self.name)
    # TODO: Add logic here
```

The missing piece is the **recursive step**: iterating over `self.subdepartments` and calling `traverse` on each unvisited child.

## The Complete Fix

```python
def traverse(self, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []
    visited.add(self.name)
    result.append(self.name)
    for subdept in self.subdepartments:       # iterate over children
        if subdept.name not in visited:       # guard against revisit
            subdept.traverse(visited, result) # recurse into child
    return result
```

## `DepartmentTree` vs Other Node Types in This Series

| Module | Node class | Child attr | Name attr | DFS style |
|--------|-----------|------------|-----------|-----------|
| `company-hierarchy-dfs` | `Node` | `.children` | `.value` | Nested helper |
| `planet-continents-dfs` | `Node` | `.children` | `.value` | Method on Node |
| `galactic-hierarchy-dfs-debug` | `TreeNode` | `.children` | `.value` | Method on Node |
| `department-tree-dfs` | `DepartmentTree` | `.subdepartments` | `.name` | **Method on Node** |

The core DFS algorithm is identical across all — only the attribute names change.

## Traversal Trace

Starting from `CEO`:

| Visit # | Node | Why |
|---------|------|-----|
| 1 | CEO | Root |
| 2 | CTO | First subdept of CEO |
| 3 | Infrastructure | First subdept of CTO |
| 4 | App Development | Second subdept of CTO |
| 5 | Security | Third subdept of CTO |
| 6 | CFO | Second subdept of CEO (backtrack) |
| 7 | Accounting | First subdept of CFO |
| 8 | Investor Relations | Second subdept of CFO |
| 9 | COO | Third subdept of CEO (backtrack) |

## Complexity Analysis

| Measure | Value | Reasoning |
|---------|-------|-----------|
| **Time** | **O(n)** | Each node visited exactly once |
| **Space** | **O(n)** | `visited` set + O(h) call stack |
