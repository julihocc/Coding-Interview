# Algorithm Analysis: Binary Tree In-Order Traversal

## Background: Tree Traversal Orders

A **traversal** visits every node in a tree exactly once. For binary trees, three classic depth-first orders exist:

| Traversal  | Visit Order                         | Example output for lesson tree |
|------------|-------------------------------------|-------------------------------|
| In-order   | Left → Root → Right                 | 4, 2, 5, 1, 3, 6              |
| Pre-order  | Root → Left → Right                 | 1, 2, 4, 5, 3, 6              |
| Post-order | Left → Right → Root                 | 4, 5, 2, 6, 3, 1              |

## 1. Recursive Approach

The recursive solution directly encodes the traversal definition:

```
in_order(node):
    if node is None: return
    in_order(node.left)   # visit left subtree
    record node.value     # visit root
    in_order(node.right)  # visit right subtree
```

### Complexity Analysis

- **Time Complexity**: **O(n)** — Every node is visited exactly once.
- **Space Complexity**: **O(h)** — The call stack depth equals the tree height `h`.
  - Best case (balanced tree): `h = O(log n)`
  - Worst case (skewed/chain tree): `h = O(n)`

## 2. Iterative Approach (Explicit Stack)

An iterative solution simulates the call stack manually using an explicit stack, which can be useful when recursion depth is a concern.

```
stack = [], result = [], node = root
while node or stack:
    while node:
        stack.push(node)
        node = node.left
    node = stack.pop()
    result.append(node.value)
    node = node.right
```

### Complexity Analysis

- **Time Complexity**: **O(n)**
- **Space Complexity**: **O(h)** — same reasoning as the recursive approach.

## 3. Key Tree Facts (from the lesson)

- A tree with `n` nodes has exactly `n - 1` edges (`E = V - 1`).
- Trees are **acyclic** (no cycles) and **connected**.
- For a perfectly balanced binary tree, operations run in **O(log n)** time.
- For a worst-case skewed tree, operations degrade to **O(n)** time.

## Corner Cases

- **Empty tree (`root = None`)**: Return an empty list `[]`.
- **Single node**: Return a list with just that one value.
- **Left-only or right-only chain**: Traversal still works; space complexity degrades to O(n).
