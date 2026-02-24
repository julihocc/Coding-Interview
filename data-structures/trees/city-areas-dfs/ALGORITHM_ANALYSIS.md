# Algorithm Analysis: City Areas DFS — Build and Traverse from Scratch

## What This Exercise Covers

This is the **capstone** exercise of the DFS series: students must implement *both* the tree construction logic (`add_area`) and the DFS traversal (`dfs`) from scratch using only the TODO comments as guidance.

## Completing `add_area`

```python
def add_area(self, area_name):
    self.areas.append(CityNode(area_name))
```

Creates a new `CityNode` for the area and appends it to `self.areas`. O(1).

## Completing `dfs`

```python
def dfs(self, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []
    visited.add(self.name)
    result.append(self.name)
    for area in self.areas:
        if area.name not in visited:
            area.dfs(visited, result)
    return result
```

## Building the City Tree

```python
city = CityNode('City Center')
city.add_area('North District')
city.add_area('East District')
city.add_area('South District')

north = city.areas[0]
north.add_area('Elm Suburb')
north.add_area('Oak Suburb')

east = city.areas[1]
east.add_area('Pine Suburb')
east.add_area('Maple Suburb')

south = city.areas[2]
south.add_area('Cedar Suburb')
```

## DFS Traversal Trace

| Step | Node | Coming from |
|------|------|-------------|
| 1 | City Center | Root |
| 2 | North District | First area of City Center |
| 3 | Elm Suburb | First area of North District |
| 4 | Oak Suburb | Second area of North District |
| 5 | East District | Second area of City Center (backtrack) |
| 6 | Pine Suburb | First area of East District |
| 7 | Maple Suburb | Second area of East District |
| 8 | South District | Third area of City Center (backtrack) |
| 9 | Cedar Suburb | First area of South District |

## Summary: DFS Patterns in This Module Series

| Module | Task type | Key challenge |
|--------|-----------|---------------|
| `depth-first-search` | Learn | Understand adjacency-dict DFS |
| `company-hierarchy-dfs` | Apply | Use DFS on Node-based tree |
| `planet-continents-dfs` | Extend | Add nodes, then traverse |
| `galactic-hierarchy-dfs-debug` | Debug | Fix `self` → `child` bug |
| `department-tree-dfs` | Implement | Fill in missing loop body |
| `city-areas-dfs` | **Build from scratch** | Implement tree + DFS end-to-end |

## Complexity Analysis

| Measure | Value | Reasoning |
|---------|-------|-----------|
| **Time** | **O(n)** | Each node visited exactly once |
| **Space** | **O(n)** | `visited` + `result` + O(h) call stack |
