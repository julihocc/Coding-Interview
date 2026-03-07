# Algorithm Analysis: Maximum Subtree Height Difference

## Exploring the Problem

The problem asks for the maximum absolute difference between the heights of the left and right subtrees across all nodes in a Binary Search Tree.

To find this value, we must be able to calculate the height of any subtree.

### 1. Naive Approach (Top-Down)

A straightforward way is to traverse the tree. For each node visited, we can recursively calculate the height of its left subtree and its right subtree, find the absolute difference, and update a global/passed maximum. Then recursively do the same for the left and right children.

- **Time Complexity**: $O(n^2)$ in the worst case. For a skewed tree, calculating the height takes $O(n)$ time, and we do this for every node $O(n)$. Thus it bounds to $O(n^2)$. For a completely balanced tree, it would be $O(n \log n)$.
- **Space Complexity**: $O(n)$ in the worst case due to the recursion stack of the traversal and the height calculation.

### 2. Optimized Approach (Bottom-Up)

We can optimize this by calculating the height of each subtree and updating the maximum difference simultaneously in a single bottom-up traversal.

In a post-order traversal (visiting left child, right child, then node):

1. We recursively find the height of the left subtree.
2. We recursively find the height of the right subtree.
3. We update the maximum difference seen so far using the absolute difference of these two heights.
4. We return the height of the current node (`max(left_height, right_height) + 1`) to its parent.

This way, the height of each node is computed exactly once from the bottom up.

- **Time Complexity**: $O(n)$ - We visit each node exactly once.
- **Space Complexity**: $O(h)$ - The space complexity is bounded by the height of the tree $h$ due to the recursion stack. In the worst case (skewed tree), $O(n)$. In the best case (balanced tree), $O(\log n)$.
