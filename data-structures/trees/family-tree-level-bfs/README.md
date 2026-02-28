# Family Tree Level Breadth-First Search (BFS)

Great work, Warp-speed Codemander! Your prowess in implementing the BFS algorithm and understanding tree traversals is commendable!

However, we have a challenge: suppose you're studying the lineage of a royal family, where each node represents a family member. '1' is the current monarch, with '2', '3', and '4' their immediate heirs. Others are descendants.

Can you implement the BFS algorithm on this family tree, showing the level for each vertex, i.e., how far away each vertex is from the family tree root?

Buckle up - it's time to code!

## Problem Statement

Given a dictionary representing a family tree (as an adjacency list) and a starting root monarch, implement a Breadth-First Search (BFS) that calculates and returns the "level" of each family member from the root.

**Input:**

- `graph`: A dictionary mapping a family member ID (string) to a list of their children (strings).
- `root`: The starting monarch ID (string).

**Output:**

- Return a dictionary mapping each visited family member ID (string) to their level (integer), where the root is at level 0, their immediate children at level 1, and so on.

### Example

```python
graph = {
  '1' : ['2', '3', '4'],
  '2' : ['5', '6'],
  '3' : ['7'],
  '4' : ['8', '9'],
  '5' : [],
  '6' : ['10'],
  '7' : ['11', '12'],
  '8' : [],
  '9' : [],
  '10' : [],
  '11' : [],
  '12' : []
}

print(Solution().bfs_level(graph, '1'))
# Output: {'1': 0, '2': 1, '3': 1, '4': 1, '5': 2, '6': 2, '7': 2, '8': 2, '9': 2, '10': 3, '11': 3, '12': 3}
```
