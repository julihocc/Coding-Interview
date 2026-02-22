# Algorithm Analysis: Company Hierarchy Tree — Restructure and Traverse

## The Two Phases

This problem combines two distinct operations:

1. **Tree Search**: Find the target nodes (`"VP Engineering"`, `"Engineer"`) using DFS.
2. **Tree Modification**: Use `add_child` and `remove_child` to rewire the tree.
3. **Tree Traversal**: Return the pre-order DFS result of the restructured tree.

---

## Phase 1: Node Search (DFS)

To find a node by value, traverse all nodes using DFS:

```
find(node, target):
    if node is None: return None
    if node.value == target: return node
    for child in node.children:
        result = find(child, target)
        if result: return result
    return None
```

- **Time Complexity**: **O(n)** — must visit every node in the worst case.
- **Space Complexity**: **O(h)** — recursion depth.

---

## Phase 2: Tree Modification

| Operation            | Method         | Complexity |
|----------------------|----------------|-----------|
| Add a new child      | `add_child`    | **O(1)** amortized (list append) |
| Remove an existing child | `remove_child` | **O(k)** where k = number of children of that parent |
| Re-parent a node     | `remove_child` + `add_child` | **O(k)** + **O(1)** |

**Re-parenting `"Engineer"`**:
```
vp_eng.remove_child(engineer)    # O(k), removes from old parent
senior_eng.add_child(engineer)   # O(1), attaches to new parent
```

---

## Phase 3: Pre-Order Traversal

Visit the current node first, then each child recursively:

```
pre_order(node, result):
    result.append(node.value)
    for child in node.children:
        pre_order(child, result)
```

- **Time Complexity**: **O(n)**
- **Space Complexity**: **O(h)**

---

## Combined Complexity

| Step           | Time   | Space  |
|----------------|--------|--------|
| Search (×2)    | O(n)   | O(h)   |
| Modification   | O(k)   | O(1)   |
| Traversal      | O(n)   | O(h)   |
| **Total**      | **O(n)** | **O(h)** |

---

## Corner Cases

- **Node not found**: A robust implementation should handle the case where `"VP Engineering"` or `"Engineer"` is missing (e.g., raise `ValueError`).
- **Already restructured**: If `"Engineer"` is already under `"Senior Engineer"`, a second call should be idempotent or raise an error.
- **Empty tree**: Return `[]` immediately.
