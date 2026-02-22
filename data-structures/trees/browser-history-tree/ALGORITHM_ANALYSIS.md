# Algorithm Analysis: Browser History Tree — Pre-Order Traversal

## What is Pre-Order Traversal?

Pre-order traversal visits nodes in **Root → Children** order. For each node:
1. Visit (record) the current node's value.
2. Recursively visit each child, left to right.

This mirrors how you'd narrate your browsing session: "I opened Google, then from Google I went to CodeSignal, from CodeSignal I opened Tour and then Blog, and from Google I also opened Gmail."

## Comparing Traversal Orders on Non-Binary Trees

| Traversal   | Visit Order             | BFS/DFS | Real-world intuition        |
|-------------|-------------------------|---------|-----------------------------|
| Pre-order   | Root → Children         | DFS     | Narrating history in order  |
| Post-order  | Children → Root         | DFS     | Cleaning up (delete leaves first) |
| Level-order | Level by level (BFS)    | BFS     | Printing org chart by rank  |

For the lesson tree, pre-order yields:
```
Start → Google.com → CodeSignal.com → CodeSignal.com/Tour
     → CodeSignal.com/Blog → Gmail.com
```

## 1. Recursive Approach

```
pre_order(node, result):
    if node is None: return
    result.append(node.value)       # 1. visit root first
    for child in node.children:
        pre_order(child, result)    # 2. recurse into each child
```

### Complexity Analysis

- **Time Complexity**: **O(n)** — Every node is visited exactly once.
- **Space Complexity**: **O(h)** — The call stack depth equals the tree height `h`.
  - Balanced / wide tree: `h = O(log n)` or **O(1)** for a flat tree
  - Worst case (deep chain): `h = O(n)`

## 2. Iterative Approach (Explicit Stack)

Pre-order can also be done iteratively by pushing children onto a stack in **reverse order** so the leftmost child is processed first:

```
stack = [root]
result = []
while stack:
    node = stack.pop()
    result.append(node.value)
    for child in reversed(node.children):
        stack.append(child)
```

### Complexity Analysis

- **Time Complexity**: **O(n)**
- **Space Complexity**: **O(w)** — The stack holds at most as many nodes as the widest level.

## 3. `add_child` / `remove_child` Complexity

| Operation       | Implementation                         | Complexity |
|-----------------|----------------------------------------|-----------|
| `add_child`     | `list.append(child)` — amortized O(1) | **O(1)**  |
| `remove_child`  | List comprehension scan                | **O(k)** where k = number of children |

## Corner Cases

- **Empty tree (`root = None`)**: Return `[]`.
- **Single node**: Returned immediately, no children to recurse into.
- **Chain**: Recursion depth equals n — space is O(n).
- **Flat tree** (root with n−1 direct children): Stack / call stack depth is O(1); all children processed in one level.
