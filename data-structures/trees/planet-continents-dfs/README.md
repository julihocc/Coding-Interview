# Planet Continents DFS Traversal

## Problem Description

You are given a `Node` class where **DFS is implemented as a method** on the node itself. A planet hierarchy has been partially built:

```
Earth
├── Africa
│   ├── Nigeria
│   └── South Africa
└── Asia
    ├── China
    └── India
```

Your task is to **extend** the tree by adding **two additional countries to Africa** and **two additional countries to Asia**, then call `depth_first_search()` from the root and return the traversal order as a list.

## Expected Extended Tree

```
Earth
├── Africa
│   ├── Nigeria
│   ├── South Africa
│   ├── Egypt         ← new
│   └── Kenya         ← new
└── Asia
    ├── China
    ├── India
    ├── Japan         ← new
    └── South Korea   ← new
```

**Expected DFS Output:**

```
['Earth', 'Africa', 'Nigeria', 'South Africa', 'Egypt', 'Kenya',
 'Asia', 'China', 'India', 'Japan', 'South Korea']
```

## Constraints

- Use the `add_child` method to attach new nodes.
- DFS is implemented as `depth_first_search(self, visited=None)` on the `Node` class.
- The `visited` set prevents revisiting nodes.
- You may choose any two valid countries for each continent.

## Node Definition

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_value):
        self.children.append(Node(child_value))

    def depth_first_search(self, visited=None):
        if visited is None:
            visited = set()
        visited.add(self.value)
        for child in self.children:
            if child.value not in visited:
                child.depth_first_search(visited)
```

## Function Signature

```python
class Solution:
    def extend_and_traverse(self, root) -> list[str]:
        """Add two countries to Africa and two to Asia, return DFS traversal."""
        pass
```
