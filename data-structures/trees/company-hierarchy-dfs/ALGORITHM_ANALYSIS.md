# Algorithm Analysis: Company Hierarchy DFS Traversal

## Background: DFS on Node-Based Trees

This module uses a **`Node`-based tree** (each node holds a list of `.children`) rather than an adjacency dictionary. Since the tree is directed and acyclic (parent → children only), cycles are impossible — but we still use a `visited` set following the lesson's implementation pattern.

The traversal order is **pre-order DFS**: visit the current node *before* recursing into its children. This naturally models a *top-down* exploration of a hierarchy (head office → departments → teams).

## 1. Recursive DFS (Pre-Order)

```
def dfs(node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node.value)
    result.append(node.value)
    for child in node.children:
        if child.value not in visited:
            dfs(child, visited)
```

### Complexity Analysis

| Measure | Value | Reasoning |
|---------|-------|-----------|
| **Time** | **O(n)** | Every node is visited exactly once |
| **Space** | **O(n)** | `visited` set + O(h) call stack; worst-case chain → O(n) |

- Balanced tree height: **O(log n)** stack depth
- Linear chain height: **O(n)** stack depth

## 2. Iterative DFS (using an explicit stack)

An iterative approach avoids Python's recursion limit for very deep hierarchies:

```
def dfs_iterative(root):
    stack = [root]
    visited = set()
    result = []
    while stack:
        node = stack.pop()
        if node.value in visited:
            continue
        visited.add(node.value)
        result.append(node.value)
        # Push children in reverse order to preserve left-to-right traversal
        for child in reversed(node.children):
            if child.value not in visited:
                stack.append(child)
    return result
```

### Complexity Analysis

- **Time Complexity**: **O(n)** — each node is pushed and popped exactly once.
- **Space Complexity**: **O(n)** — the stack holds at most all nodes in the worst case.

## 3. DFS vs BFS for Hierarchies

| Property           | DFS (this module)       | BFS (non-binary-tree-traversal) |
|--------------------|-------------------------|---------------------------------|
| Explores           | Depth first             | Level by level                  |
| Data structure     | Stack (call stack)      | Queue                           |
| Output order       | Pre-order (top-down path) | Level-order                   |
| Use case           | Hierarchy paths, connectivity | Level summaries, shortest path |

## Corner Cases

- **Single node**: Returns `[root.value]` immediately.
- **Wide tree** (many children, no grandchildren): DFS still visits all children in order.
- **Deep chain** (each node has one child): Recursion depth equals `n`; iterative approach is safer for very large inputs.
