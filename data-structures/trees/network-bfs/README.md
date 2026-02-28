# Network Concept Breadth-First Search (BFS)

Well done, space explorer! You're right at the finish line! It's time to conclude our BFS practice with a final task!

Can you independently implement a Python function for Breadth-First Search (BFS)? You will be given an adjacency list representation of a graph and a root node. Your BFS function should return a list of nodes in the order they were visited.

Please follow the steps outlined in the TODO comments of the starter code and apply the knowledge you acquired from this lesson. Remember, you are the commander of this mission, so let's take it to a successful conclusion!

## Problem Statement

Given an adjacency list representing a computer network and a starting root device, implement a Breadth-First Search (BFS) that traverses the network and returns the nodes in the exact order they are visited.

**Input:**

- `tree`: A dictionary mapping a device name (string) to a list of its connected devices (strings).
- `root`: The starting device name (string).

**Output:**

- Return a list of device names (strings) in the order they were visited during the BFS traversal.

### Example

```python
tree = {
  'computer' : ['printer', 'router'],
  'printer' : ['paper', 'computer'],
  'router' : ['internet', 'computer'],
  'internet' : ['data', 'router'],
  'paper' : ['printer'],
  'data' : ['internet'],
}

print(Solution().bfs(tree, 'computer'))
# Output: ['computer', 'printer', 'router', 'paper', 'internet', 'data']
```
