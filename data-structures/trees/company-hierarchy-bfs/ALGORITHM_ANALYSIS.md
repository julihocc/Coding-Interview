# Algorithm Analysis: Company Hierarchy BFS

## Time Complexity

The time complexity for exploring the company hierarchy using Breadth-First Search (BFS) is `O(V + E)`, where `V` is the number of employees (nodes) and `E` is the number of reporting relationships (edges). Since every node is enqueued once and its adjacency list is evaluated, the complexity scales linearly with the size of the graph. In a purely tree-like structure, `E = V - 1`, therefore scaling asymptotically to `O(V)`.

## Space Complexity

The space complexity is `O(V)`. This accounts for:

1. The `queue`, which could hold up to `O(V)` elements at the widest level of the team structure.
2. The `visited` tracking list, which sequentially stores all `V` members.
