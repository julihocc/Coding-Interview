# Algorithm Analysis: Planet Continents DFS Traversal

## Background: Method-Based DFS

This module introduces a third DFS pattern: **DFS as an instance method** on the `Node` class itself. Instead of a standalone `dfs(tree, root)` function or a `Solution` class calling a helper, the traversal logic lives directly on the node. This is a common object-oriented design for tree nodes.

```python
def depth_first_search(self, visited=None):
    if visited is None:
        visited = set()
    visited.add(self.value)
    for child in self.children:
        if child.value not in visited:
            child.depth_first_search(visited)  # pass visited along!
```

> **Note on the lesson's starter code**: The original lesson code had a subtle bug —
> `child.depth_first_search()` was called without passing `visited`, which would reset
> the visited set on every recursive call. The corrected form passes `visited` explicitly:
> `child.depth_first_search(visited)`.

## DFS Traversal Order

Starting from `Earth`, DFS visits nodes in **pre-order** (parent before children):

```
Earth → Africa → Nigeria → South Africa → Egypt → Kenya
                                        → Asia → China → India → Japan → South Korea
```

This mirrors a depth-first exploration: fully traversing Africa (and all its countries) before moving on to Asia.

## add_child Pattern

```python
def add_child(self, child_value):
    self.children.append(Node(child_value))
```

`add_child` creates a new `Node` internally and appends it to `self.children`. This keeps tree construction clean but means you must access `root.children[i]` by index (or by searching by value) to reach a specific node for further expansion.

### Complexity Analysis

| Measure | Value | Reasoning |
|---------|-------|-----------|
| **Time** (DFS) | **O(n)** | Every node visited exactly once |
| **Space** (DFS) | **O(n)** | `visited` set + O(h) call stack |
| **add_child** | **O(1)** | Append to list |

## Patterns Compared Across Modules

| Module | Node type | DFS style | Tree rep |
|--------|-----------|-----------|----------|
| `depth-first-search` | `str` labels | Standalone function | Adjacency dict |
| `company-hierarchy-dfs` | `Node` objects | Nested helper in `Solution` | Node + `.children` |
| `planet-continents-dfs` | `Node` objects | **Method on `Node` itself** | Node + `.children` |

## Corner Cases

- **`visited` not passed at recursive call site**: causes infinite recursion if there are shared references; always pass `visited` down.
- **Single continent, no countries**: DFS returns `['Earth', 'ContinentName']`.
- **Country added twice under same continent**: duplicate values in `visited` guard against revisiting.
