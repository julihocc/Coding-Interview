# Algorithm Analysis: BST Interview Problems

This module covers two important interview problems related to Binary Search Trees. Below is the analysis of the optimal approaches discussed in the lesson.

## Problem 1: Checking the Balance of a Binary Search Tree (is_balanced)

### Time Complexity: $O(n)$

The optimal solution computes the heights of the subtrees and simultaneously checks the balance condition using recursion. Each node in the tree is visited at most exactly once. The work done at each node (checking max height, calculating absolute differences, and simple arithmetic) takes $O(1)$ constant time. Therefore, the overall time complexity is linearly proportional to the number of nodes, $n$.

*Note*: Early termination (`is_balanced = False`) might allow returning even before visiting all vertices if an unbalanced state is encountered, but the worst-case scenario entails visiting all $n$ nodes.

### Space Complexity: $O(h)$

The space complexity corresponds to the maximum recursion stack depth, which is the height of the tree $h$.

- **Best/Average Case** (Balanced Tree): $O(\log n)$ space for the recursion stack.
- **Worst Case** (Skewed Tree): $O(n)$ space when the tree degenerates into a sparse, linked-list-like structure.

---

## Problem 2: Identify the K-th Smallest Element in a BST (kthSmallest)

### Time Complexity: $O(h + k)$

The algorithmic approach utilizes the property of the BST along with the count of nodes per subtree.

- Tracing down the tree structure to find the k-th smallest requires exploring paths from the root to the target element.
- Calculating the node count (`countNodes`) for an entire subtree takes time proportional to the number of descendants. However, the recursive approach ensures that as we descend down, we only count the structures we absolutely need.
- In the worst case, searching recursively will cost time bounded up to examining $k$ key vertices. So the total worst-case time is roughly bounded around $O(h + k)$, which could degenerate to $O(n)$ if the tree is skewed and $k \approx n$. An alternate in-order iterative approach with early stopping precisely guarantees an $O(h + k)$ complexity.

### Space Complexity: $O(h)$

Space complexity matches the maximum depth of the call stack required to hold the active recursive calls of both `kthSmallest` and `countNodes`.

- **Best/Average Case** (Balanced Tree): Recursion reaches depth proportional to $O(\log n)$.
- **Worst Case** (Skewed Tree): Recursion requires a call frame for all elements down to the element of interest, leading to $O(n)$ space.

### Alternative (Iterative In-Order Traversal approach)

An iterative in-order traversal stops after checking $k$ elements, retaining equivalent complexities: $O(h + k)$ Time cost and $O(h)$ extra memory cost. The provided counting algorithm is highly favored if subtree frequencies were pre-calculated and cached at each node (yielding explicit $O(\log n)$ time answers).
