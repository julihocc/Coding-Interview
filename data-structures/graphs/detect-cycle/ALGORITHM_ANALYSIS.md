# Algorithm Analysis: Detect Cycles in an Undirected Graph

## Exploring the Problem

The problem asks us to determine if an undirected graph contains any cycles. A cycle is a path of edges and vertices wherein a vertex is reachable from itself. Importantly, we must handle disconnected graphs, meaning we cannot assume every node is reachable from an arbitrary starting node.

### Approach: Depth-First Search (DFS)

We can use Depth-First Search (DFS) to traverse the graph. To identify a cycle in an undirected graph during DFS:
1. We keep track of visited vertices to avoid infinite loops and duplicate processing.
2. When visiting a neighbor of the current vertex, if the neighbor is already in the `visited` set, it might be a cycle.
3. However, since the graph is undirected, every edge `A-B` appears twice (once as `A` to `B`, and once as `B` to `A`). Thus, if `B` sees `A` as a visited neighbor, it's not a cycle if `A` was the immediate `parent` that led us to `B`.
4. Therefore, we only report a cycle if we encounter a visited neighbor that is **not** the immediate parent of the current vertex.

To handle disconnected graphs, we must iterate over *all* vertices in the graph and initiate a DFS from any unvisited vertex. This ensures all components are checked.

### Complexity Matrix

- **Time Complexity**: $O(V + E)$
  - $V$ is the number of vertices and $E$ is the number of edges.
  - In the worst case, we visit every vertex once and examine every edge once (or twice, since it's undirected). The outer loop ensures we process all vertices, and the inner DFS explores their reachable edges.
- **Space Complexity**: $O(V)$
  - In the worst case, the recursion stack could go as deep as the number of vertices $V$ (e.g., in a skewed graph like a line).
  - The `visited` set will also store up to $V$ vertices.
  - Therefore, the auxiliary space complexity is $O(V)$.
