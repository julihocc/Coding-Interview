= Trees

A Tree is a hierarchical, non-linear data structure consisting of nodes connected by edges. It represents relationships where one node is considered the "parent" and the nodes below it are its "children". A tree has a single root node and no cycles.

== Binary Trees
A Binary Tree is a tree where each node has at most two children, referred to as the left child and the right child.

== Tree Traversals

When we want to visit every node in a tree, we typically use one of two main strategies: Depth-First Search (DFS) or Breadth-First Search (BFS).

=== Depth-First Search (DFS)
DFS prioritizes going as deep as possible down a single path before backtracking. It is naturally implemented using recursion (which implicitly uses the system call stack) or iteratively using an explicit stack.

There are three main DFS traversals for binary trees, named by the position of the current node relative to its children:

- *Pre-order (Current, Left, Right):* Useful for creating copies of a tree or serializing a tree structure.
- *In-order (Left, Current, Right):* For a Binary Search Tree (BST), an in-order traversal visits all the nodes in sorted ascending order.
- *Post-order (Left, Right, Current):* Useful for deleting a tree from the bottom up, or calculating the height/size of a tree based on its children's values.

=== Breadth-First Search (BFS)
BFS prioritizes exploring all neighbors (children) at the current depth level before moving deeper. It is implemented iteratively using a Queue.

- *Level-order Traversal:* Visit the root, then both children of the root (level 1), then all four grandchildren (level 2), and so on.
- *Why BFS?* It is guaranteed to find the shortest path from the root to any other node in an unweighted tree or graph.

== Time and Space Complexity
For a tree with $n$ nodes and a height of $h$:
- *Time Complexity:* Both DFS and BFS visit every node exactly once, resulting in $O(n)$ time.
- *Space Complexity:*
  - *DFS:* Takes $O(h)$ space on the call stack. In the worst-case (a skewed tree that acts like a linked list), $h = n$, so space is $O(n)$. In a perfectly balanced tree, $h = log n$.
  - *BFS:* Takes $O(w)$ space where $w$ is the maximum width of the tree. In a perfectly balanced tree, the last level has almost half the nodes, making space $O(n)$.
