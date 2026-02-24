# Algorithm Analysis: Depth-First Search (DFS) on Trees

## Background: DFS Strategy

**Depth-First Search (DFS)** is a tree/graph traversal strategy that explores as **deep as possible** along each branch before backtracking. Think of it like navigating a labyrinth: follow one path all the way to its end before turning back to try another.

Key properties:

- Uses **recursion** (or an explicit stack) to track the current path.
- A **visited set** prevents revisiting nodes — essential when using a bidirectional adjacency representation.
- Unlike BFS, DFS does not guarantee shortest paths.

## 1. Recursive DFS Traversal

The recursive approach mirrors the algorithm's natural description: visit a node, then recursively visit each unvisited neighbor.

```
def dfs(tree, root, visited, traversal):
    traversal.append(root)
    visited.add(root)
    for child in tree[root]:
        if child not in visited:
            dfs(tree, child, visited, traversal)
```

### Complexity Analysis

- **Time Complexity**: **O(V + E)** — Every vertex (V) and edge (E) is visited at most once.
  - For trees where **E = V − 1**, this simplifies to **O(V)**.
- **Space Complexity**: **O(V)** — The `visited` set holds up to V entries; the call stack depth equals the tree height `h`.
  - Balanced/bushy tree: **O(log V)**
  - Linear chain: **O(V)**

## 2. DFS Path Finding

A common DFS application is finding a path between two nodes. The algorithm builds the path incrementally and returns early once the target is reached.

```
def find_path(tree, start, end, visited, path=[]):
    path = path + [start]
    visited.add(start)
    if start == end:
        return path
    for node in tree[start]:
        if node not in visited:
            new_path = find_path(tree, node, end, visited, path)
            if new_path:
                return new_path
    return None
```

### Complexity Analysis

- **Time Complexity**: **O(V + E)** — In the worst case, DFS visits all nodes before finding the target.
- **Space Complexity**: **O(V)** — The `path` list and `visited` set each grow up to V entries; the call stack adds O(h).

## 3. DFS vs BFS at a Glance

| Property              | DFS                        | BFS                          |
|-----------------------|----------------------------|------------------------------|
| Data Structure        | Stack (call stack / explicit) | Queue                      |
| Traversal order       | Depth-first                | Level-by-level               |
| Shortest path?        | No (for unweighted graphs) | Yes (for unweighted graphs)  |
| Time Complexity       | O(V + E)                   | O(V + E)                     |
| Space Complexity      | O(h) call stack            | O(w) queue width             |

## Corner Cases

- **Single node, no neighbors**: DFS returns `[root]` immediately.
- **Disconnected components**: DFS only visits nodes reachable from `root`.
- **Path not found**: `find_path` returns `None` when no path exists between `start` and `end`.
- **Start equals end**: `find_path` returns `[start]` immediately.
