# Algorithm Analysis: Binary Tree From Scratch — Build and In-Order Traverse

## Recap: Binary Tree Terminology

| Term        | Definition                                              |
|-------------|---------------------------------------------------------|
| Root        | The topmost node (no parent) — `Node(4)` in our tree   |
| Leaf        | A node with no children — `1`, `3`, `5`, `7`           |
| Height      | Max depth of any leaf — `2` for the balanced tree      |
| Subtree     | Any node and its descendants                            |
| BST property| Left child < parent < right child                       |

## Phase 1: Defining the Node Class

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None   # left child
        self.right = None   # right child
```

- **Space per node**: O(1) — stores one value and two pointers.
- **Total space for n nodes**: O(n).

## Phase 2: Building the Tree

Explicit pointer assignment:

```python
root       = Node(4)
root.left  = Node(2);  root.right = Node(6)
root.left.left  = Node(1);  root.left.right  = Node(3)
root.right.left = Node(5);  root.right.right = Node(7)
```

- **Time Complexity**: O(n) — n assignments for n nodes.
- **Space Complexity**: O(n) — n Node objects allocated.

## Phase 3: In-Order Traversal

```
in_order(node):
    if node is None: return
    in_order(node.left)       # 1. left subtree
    record node.value         # 2. current node
    in_order(node.right)      # 3. right subtree
```

- **Time Complexity**: **O(n)** — each node visited exactly once.
- **Space Complexity**: **O(h)** — call stack depth equals tree height `h`.
  - Balanced tree (this problem): `h = log₂(n)` → **O(log n)**.
  - Worst case (skewed chain): `h = n` → **O(n)**.

## In-Order vs Other Orders (Comparison Table)

| Traversal  | Order                | Output on lesson tree | Typical use          |
|------------|----------------------|-----------------------|----------------------|
| In-order   | Left → Root → Right  | [1,2,3,4,5,6,7]       | Sort / validate BST  |
| Pre-order  | Root → Left → Right  | [4,2,1,3,6,5,7]       | Copy / serialize     |
| Post-order | Left → Right → Root  | [1,3,2,5,7,6,4]       | Delete / evaluate    |

## Key Insight: BST + In-Order = Sorted Output

For any Binary Search Tree, in-order traversal always produces a **sorted** list.
This is why in-order traversal is the standard way to verify the BST property.

## Corner Cases

- **Empty tree (`root = None`)**: Return `[]`.
- **Single node**: Return `[node.value]` — no recursion needed.
- **Unbalanced tree**: Algorithm still correct, but O(n) space.
