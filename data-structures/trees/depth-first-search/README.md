# Depth-First Search (DFS) on Trees

## Problem Description

Given a tree represented as an **adjacency dictionary** (where each key is a node label and its value is a list of neighboring nodes), implement **Depth-First Search (DFS)** starting from a given root node and return the traversal order as a list.

DFS explores **as far down a branch as possible** before backtracking to explore other branches.

## Examples

**Example 1:** (the tree from the lesson)

```
          A
        / | \
       B  C  D
      / \   / \
     E   F G   H
        / \
       I   J
```

```
Input: root = 'A'
Output: ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'H']
```

**Example 2:** Path finding from 'A' to 'J'

```
Input: start = 'A', end = 'J'
Output: ['A', 'B', 'F', 'J']
```

**Example 3:** Single node

```
Input: tree = {'X': []}, root = 'X'
Output: ['X']
```

## Constraints

- The tree has between 1 and 100 nodes.
- Node labels are unique strings.
- The adjacency dictionary includes bidirectional connections (both parent→child and child→parent edges are listed).
- The `visited` set prevents revisiting nodes and infinite loops.

## Tree Representation

```python
tree = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    # ... (bidirectional adjacency)
}
```

## Function Signatures

```python
class Solution:
    def dfs(self, tree: dict, root: str) -> list[str]:
        """Return nodes in DFS traversal order."""
        pass

    def find_path(self, tree: dict, start: str, end: str) -> list[str] | None:
        """Return the path from start to end using DFS, or None if unreachable."""
        pass
```
