# City Areas DFS Traversal — Build and Traverse from Scratch

## Problem Description

You are a city planner mapping the areas of a city. Using a tree structure, model the city's areas (City Center and its districts/suburbs) and implement a **Depth-First Search (DFS)** traversal to visit every area.

Your task has **two parts**:

1. **Build the tree** representing the city's areas.
2. **Implement DFS traversal** to visit all areas depth-first.

## The City Hierarchy

```
City Center
├── North District
│   ├── Elm Suburb
│   └── Oak Suburb
├── East District
│   ├── Pine Suburb
│   └── Maple Suburb
└── South District
    └── Cedar Suburb
```

**Expected DFS Output:**

```
['City Center', 'North District', 'Elm Suburb', 'Oak Suburb',
 'East District', 'Pine Suburb', 'Maple Suburb',
 'South District', 'Cedar Suburb']
```

## Starter Code (with TODOs)

```python
class CityNode:
    def __init__(self, name):
        self.name = name
        self.areas = []

    def add_area(self, area_name):
        # TODO: Create a new CityNode and append it to self.areas
        pass

    def dfs(self, visited=None, result=None):
        # TODO: Initialize visited and result if None
        # TODO: Mark this node as visited and add name to result
        # TODO: For each area in self.areas, recurse if not visited
        pass

# TODO: Build the city tree
# TODO: Add North District, East District, South District to City Center
# TODO: Add Elm Suburb and Oak Suburb to North District
# TODO: Add Pine Suburb and Maple Suburb to East District
# TODO: Add Cedar Suburb to South District

# TODO: Call dfs() and print the result
```

## Constraints

- Use `self.name` as the node identifier.
- Use `self.areas` to store child nodes.
- A `visited` set must be passed through the recursion.
- The traversal order must be **pre-order DFS** (parent before children).

## Function Signature

```python
class Solution:
    def build_and_traverse(self) -> list[str]:
        """Build the city tree and return DFS traversal order."""
        pass
```
