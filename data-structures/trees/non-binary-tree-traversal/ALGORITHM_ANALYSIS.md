# Algorithm Analysis: Non-Binary Tree Level-Order Traversal

## Background: Multi-Way Trees

A **non-binary (multi-way) tree** is a rooted tree where each node can have an **arbitrary number of children**. Instead of `.left` and `.right` pointers, each node holds a list `.children`.

Key structural facts (from the lesson):
- **E = V − 1**: A tree with `n` nodes has exactly `n − 1` edges.
- Trees are **acyclic** and **connected**.
- Insertion may be O(1) if we track the insertion point; otherwise O(n).

## 1. Iterative BFS (Level-Order) Approach

BFS uses a queue to process nodes level by level. This naturally produces a level-order output.

```
queue = deque([root])
result = []
while queue:
    node = queue.popleft()
    result.append(node.value)
    for child in node.children:
        queue.append(child)
return result
```

### Complexity Analysis

- **Time Complexity**: **O(n)** — Every node is enqueued and dequeued exactly once.
- **Space Complexity**: **O(w)** — The queue holds at most `w` nodes at a time, where `w` is the maximum **width** (number of nodes at any single level).
  - Worst case: a flat tree (root with all nodes as direct children) → `w = n − 1`, so **O(n)**.
  - Best case: a chain → `w = 1`, so **O(1)** extra space.

## 2. Recursive DFS Approach (Pre-Order)

For comparison, a depth-first approach visits the root first, then recursively visits each child:

```
def dfs(node, result):
    if node is None: return
    result.append(node.value)
    for child in node.children:
        dfs(child, result)
```

This produces **pre-order DFS** output (root before children), not level-order.

### Complexity Analysis

- **Time Complexity**: **O(n)**
- **Space Complexity**: **O(h)** — Recursion depth equals the tree height `h`.
  - Balanced tree: **O(log n)**
  - Chain (single path): **O(n)**

## 3. Operations: Insertion and Deletion

From the lesson's `TreeNode` implementation:

| Operation      | Approach                                                   | Complexity |
|----------------|------------------------------------------------------------|-----------|
| `add_child`    | Append to `children` list                                  | **O(1)**  |
| `remove_child` | Filter `children` list (list comprehension)                | **O(k)**  where k = number of children |
| Search         | Must traverse all nodes in the worst case                  | **O(n)**  |
| Insertion (no tracking) | Traverse to find the insertion point                | **O(n)**  |
| Insertion (tracking)    | Direct append via stored reference                  | **O(1)**  |

## Corner Cases

- **Empty tree (`root = None`)**: Return `[]`.
- **Single node, no children**: Return `[root.value]`.
- **Wide tree** (root with many children, no grandchildren): BFS still works correctly.
- **Deep chain** (each node has exactly one child): BFS processes one node per iteration.
