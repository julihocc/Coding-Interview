# Algorithm Analysis: K-th Largest Element in a BST

## Exploring the Problem

The problem requires us to find the $k$-th largest element in a Binary Search Tree. This is a common variation of the $k$-th *smallest* problem, which leverages an in-order traversal (Left, Node, Right) to visit elements in ascending order. To find the $k$-th *largest* element, we can perform a **Reverse In-Order Traversal** (Right, Node, Left) to visit elements in strictly descending order.

### 1. Naive Approach (List Collection)

A simple approach is to traverse the entire tree (in-order or reverse in-order) and append all its values to an array. Once the traversal is complete, we simply return the $k$-th element from the end of the array (or the $k$-th element if we traversed in reverse in-order).

- **Time Complexity**: $O(n)$ where $n$ is the number of nodes. We must visit every node to build the list.
- **Space Complexity**: $O(n)$ to store all values in the list.

### 2. Optimized Approach (Reverse In-Order Traversal)

Instead of storing all elements, we can maintain a counter during our reverse in-order traversal (Right, Node, Left).

1. Traverse to the right subtree.
2. Visit the current node: increment the counter. If the counter equals $k$, we have found our answer; store it and terminate further traversal.
3. Traverse to the left subtree.

This avoids storing the full list and stops as soon as the element is found.

- **Time Complexity**: $O(h + k)$ where $h$ is the height of the tree. To reach the rightmost (largest) node, we perform $O(h)$ steps. Then, we process exactly $k$ nodes. In the worst case (skewed tree and $k=n$), this is $O(n)$. For a balanced tree on average, finding a small $k$ is very fast.
- **Space Complexity**: $O(h)$ for the recursion stack space, where $h$ is the height of the tree. In the worst case, $O(n)$ for a skewed tree, and $O(\log n)$ for a balanced tree. This is more efficient than $O(n)$ auxiliary space of the naive approach.
