# Algorithm Analysis: Planetary Network BFS

## Time Complexity

The time complexity for exploring all connected components using Breadth-First Search (BFS) is `O(V + E)`, where `V` is the number of vertices (planets) and `E` is the number of edges (connections). In a strict tree scenario where `E = V - 1`, the time complexity simplifies to `O(V)`.

## Space Complexity

The space complexity is `O(V)`. This accounts for:

1. The `queue` used to hold the next nodes to process. At the leaf level of a wide tree, it could hold up to `O(V)` elements.
2. The `visited` tracking list, which at the end of the traversal will hold all `V` elements.

This algorithm works exceptionally well for exploring immediate neighbors before venturing deeper into an interconnected domain.
