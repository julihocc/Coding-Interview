# Algorithm Analysis: Family Tree Level BFS

## Time Complexity

The time complexity for exploring the family tree and finding the level of each node using Breadth-First Search (BFS) is `O(V + E)`, where `V` is the number of family members (nodes) and `E` is the number of parent-child relationships (edges). Every node is dequeued once, and we iterate over its children to assign their levels. In a standard tree, this is bounded by `O(V)`.

## Space Complexity

The space complexity is `O(V)`. This accounts for:

1. The `queue`, which could hold up to `O(V)` elements simultaneously depending on the width of the tree.
2. The `visited` tracking list (if used).
3. The `level` dictionary returned as the final result, which definitively stores `V` key-value pairs (one for each reachable node).
