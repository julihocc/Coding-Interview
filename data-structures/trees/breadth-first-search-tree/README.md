# Exploring Breadth-first Search Algorithm on Trees

## Theory and Practice in Python

Welcome back, scholars! In today's session, we're diving deeply into the Breadth-first Search (BFS) Algorithm, specifically focusing on its application to trees. This potent search algorithm explores nodes level-by-level, examining all siblings before moving on to the children. By the end of our session, you'll have mastered the key aspects of BFS and its intricacies and will have become comfortable implementing BFS for traversing trees using Python.

To put this into context, imagine that you're navigating your way through a network of interconnected destinations, with each destination being a node in a tree. BFS is like taking a comprehensive sightseeing tour that starts at a landmark and visits all the destinations within the immediate vicinity before moving on to the next layer of destinations. With BFS, you ensure you've explored all the sights at each depth before venturing further.

### Understanding the Concept of Breadth-first Search

Breadth-first Search (BFS) is a traversal algorithm used in graphs or tree structures — it's a specific way in which we can visit nodes. When we talk about 'visiting' nodes in BFS, we aim to visit nodes closest to the root node first before moving deeper into the tree. BFS, compared to Depth-first Search (DFS), is like exploring your neighborhood before moving on to the next town, while DFS would be like driving straight across the country, visiting towns en route, before coming back to your neighboring town.

BFS is an intuitive method that can form the basis for many algorithms in graph theory. For example, it is leveraged in algorithms for finding the shortest path in unweighted graphs, network broadcasting, and games and puzzles such as the Rubik's cube.

### Visualizing Breadth-first Search

Let's create a visualization to illustrate the BFS technique. Imagine a tree structure representing a family lineage — a root node representing an ancestor and subsequent layers representing descendant generations. Starting from the ancestor, a BFS traversal visits all his immediate offspring before moving on to the grandchildren, then the great-grandchildren, and so on in cascading circles. This visualization helps illustrate how BFS explores nodes — it's like taking a layered tour of a genealogical tree!

A crucial aspect to consider in BFS is the usage of a queue. The queue is a data structure that holds the nodes still to be visited, and it follows a First In, First Out (FIFO) protocol — think of it as standing in line; the first one to get in is the first one to get out.

### BFS Algorithm Explained

Conceptually, the BFS algorithm isn't overly complicated. It starts at the root and visits all direct children before moving deeper into the tree. The algorithm can be summed up as follows:

1. Start with the root node.
2. Visit the root node and add all its direct children to the queue.
3. Visit each node in the queue, adding all its unvisited children to the queue. Repeat this exercise until the queue is empty.

This algorithm guarantees that every node on level L (on distance L from the root node) will be processed (i.e., taken from the queue) earlier than any node on level L + 1 or further, which is what we are looking for.

### Problem Statement

Given a tree represented as a dictionary where each key-value pair denotes a node and its children, implement the Breadth-first Search (BFS) algorithm to traverse the tree.

**Input:**

- `tree`: A dictionary mapping node names (strings) to lists of child node names.
- `root`: The name (string) of the root node to start the traversal from.

**Output:**

- Return a list of node names in the order they were visited during the BFS traversal.

### Example

```python
# Tree definition
tree = {
  'A' : ['B', 'C', 'D'],
  'B' : ['A', 'E'],
  'C' : ['A', 'F','G'],
  'D' : ['A', 'H'],
  'E' : ['B', 'I'],
  'F' : ['C'],
  'G' : ['C', 'J'],
  'H' : ['D'],
  'I' : ['E'],
  'J' : ['G']
}

print(Solution().bfs(tree, 'A'))
# Output: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
```
