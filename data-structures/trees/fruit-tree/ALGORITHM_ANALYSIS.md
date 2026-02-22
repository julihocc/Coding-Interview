# Algorithm Analysis: Fruit Tree — Insert Node and Pre-Order Traversal

## Problem Phases

### Phase 1: DFS Search for the Target Node

To insert at the correct location we must first **find** `"Pear"` by searching the tree:

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
- **Space Complexity**: **O(h)** — recursion depth equals tree height `h`.

### Phase 2: Insertion via `add_child`

Once the target node is found, insert the new child:

```
pear_node.add_child(TreeNode("Plum"))
```

- **Time Complexity**: **O(1)** amortized — list `.append()`.
- **Space Complexity**: **O(1)** — one new node created.

### Phase 3: Pre-Order Traversal (`print_tree` equivalent)

Visit the current node first, then recurse through each child:

```
pre_order(node, result):
    result.append(node.value)   # root first
    for child in node.children:
        pre_order(child, result)
```

- **Time Complexity**: **O(n)** — every node visited once.
- **Space Complexity**: **O(h)** — call stack depth.

## Combined Complexity

| Phase       | Time    | Space  |
|-------------|---------|--------|
| DFS Search  | O(n)    | O(h)   |
| Insertion   | O(1)    | O(1)   |
| Traversal   | O(n)    | O(h)   |
| **Total**   | **O(n)**| **O(h)**|

## Comparing with the Company Hierarchy Module

| Aspect              | `fruit-tree`     | `company-hierarchy-tree`      |
|---------------------|------------------|-------------------------------|
| Search targets      | 1 node (Pear)    | 2 nodes (VP Eng + Engineer)   |
| Modification        | Insert only      | Remove + insert (re-parent)   |
| Traversal           | Pre-order        | Pre-order                     |

## Corner Cases

- **Target node absent**: If `"Pear"` is not in the tree, insertion is skipped and a plain traversal is returned.
- **Empty tree**: Return `[]` immediately.
- **Pear already has children**: `"Plum"` is simply appended to the existing list.
