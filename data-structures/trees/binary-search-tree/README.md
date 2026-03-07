# Mastering Binary Search Trees: Understanding, Implementation, and Application in Python

## Introduction

Dear students, today's session is an exciting journey into the world of Binary Search Trees (BSTs)! Up until now, in our Understanding and Using Trees in Python course, you've gained extensive knowledge about a variety of tree structures, explored the Breadth-First Search (BFS) and Depth-First Search (DFS), and learned about Heaps in detail. Today, we're progressing to another fundamental subject that leverages the tree structure to optimize data storage and searching processes — the Binary Search Tree (BST).

In essence, Binary Search Trees are excellent data structures that optimize search operations by appropriately arranging data elements based on certain properties. These trees' "left-small, right-large" order property helps ensure fast search, insertion, and deletion operations. Essentially, BSTs are tree structures designed to make data retrieval and storage efficient and simpler.

The ultimate goal of today's lesson is three-fold. First, we will understand the intricate workings of BSTs; then, we will implement them in Python using the CodeSignal IDE, and finally, we'll apply this knowledge to solve complex algorithmic problems leveraging BSTs. So, without further ado, let's set out on this exciting exploration of BSTs!

## Understanding Binary Search Trees

Binary Search Trees (BSTs) are named for their binary nodal structure, where each node links to two child nodes — much like a binary tree. However, what differentiates them is a crucial property ingrained in them: every node ensures that the values in its left subtree are less than or equal to its value, and the values in its right subtree are greater than its value. This property facilitates highly efficient search operations.

Let's illuminate this concept with a simple instance. Take a look at the BST below - note that for every node, all elements in the left subtree are smaller than the node value, and all elements in the right subtree are larger than the node value.

```
        5
       / \
      3   9
     / \ /
    1  4 6
```

Here, `5` sits at the root of the tree, its left subtree contains values `1`, `3`, and `4`, all less than the root value `5`, and the right subtree contains values `6` and `9`, both larger than `5`. The same condition holds for all other nodes in the tree. This simple example provides a clear insight into the underlying logic that governs the BST's node placement.

## BST Operations

### Insertion

To maintain the key BST property during insertion, a new value `x` must be carefully positioned. We start at the root and traverse down the BST. If `x` is less than the current node's value, we go left; if it's greater, we move to the right child. We continue this movement until we find an appropriate spot devoid of a child node, where we place `x` in a new node at that location.

### Searching

Searching will help us find if a value exists in the BST. We start at the root and traverse down the tree until we find the key. If the key's value is greater than a node's value, we move right, and if it's smaller, we move left. If we can't locate the key or the tree is empty, our function returns `None`, indicating that the key is not present in the BST.

### Deletion

Deleting a node can be a bit tricky because you must maintain the BST property even after the deletion. A node can be deleted following these steps:

1. If the node is a leaf node, delete the node outright.
2. If the node has only one child: Replace the node with its subtree.
3. If the node has both children: Find its in-order successor (the smallest value in its right subtree) or its in-order predecessor (the largest value in its left subtree) and replace the node with that value. After replacing, delete the in-order successor or predecessor node.

## Node Definition

```python
class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
```

## Problem Description

Implement a `BinarySearchTree` class that performs basic operations on a BST using the `Node` structure defined above. Keep track of the root of the tree and return it or the result of operations accordingly.

1. `insert(val)`: Inserts a new value into the BST and returns the new root.
2. `search(val)`: Searches for a value in the BST and returns the `Node` containing the value, or `None` if not found.
3. `delete(val)`: Deletes the given value from the BST and returns the new root.

## Constraints

- `0 <= number of nodes <= 10^4`
- `-10^5 <= val <= 10^5`
- Values inserted will be unique, but searches and deletions may query values not in the tree.

## Function Signature

```python
class Solution:
    def __init__(self):
        self.root = None

    def insert(self, val: int) -> 'Node':
        pass

    def search(self, val: int) -> 'Node':
        pass

    def delete(self, val: int) -> 'Node':
        pass
```
