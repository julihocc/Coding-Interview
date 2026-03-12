# Detect Cycles in an Undirected Graph

## Problem Statement

Think of an undirected graph, like a cosmic web of stars and galactic highways. Imagine you're a space entity trying to find closed circuits, or cycles, from a star back to itself without retracing any pathway.

Your mission is to create a function `has_cycle(graph)` that checks if there are any cycles in the graph. But here is the catch: not all the stars are connected with others with space routes, and there is a possibility that the given graph is disconnected. It basically means that there could be two or more vertices that have no path from one to another at all!

Modify the cycle-detecting algorithm to handle such cases.

### Example 1

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['C'],
    'E': ['G', 'K'],
    'K': ['G', 'E'],
    'G': ['K', 'E']
}
# Output: True
```

**Explanation:** There is a cycle `E-G-K-E` in the second connected component of the graph.

## Function Signature

```python
from typing import Dict, List

class Solution:
    def has_cycle(self, graph: Dict[str, List[str]]) -> bool:
        pass
        
    def dfs(self, vertex: str, visited: set, graph: Dict[str, List[str]], parent: str) -> bool:
        pass
```
