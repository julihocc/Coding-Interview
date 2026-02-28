# Company Hierarchy Breadth-First Search (BFS)

Great work on your BFS tasks! You've excelled in traversing trees. However, let's delve a little deeper. Imagine that you're managing a company's team tree chart. Each node represents a staff member. Here, '1' is the CEO, with '2', '3', and '4' as managers, and the remainder are team members.

Your goal is to follow the chain of command from the top down, starting with the CEO. However, the provided initial code wasn't producing the correct output. Your task is to identify and correct the problem to properly perform a Breadth-First Search.

## Problem Statement

Given a dictionary representing a company's team tree chart (as an adjacency list) and a starting root node, implement a corrected Breadth-First Search (BFS) to traverse the company hierarchy top-down.

**Input:**

- `graph`: A dictionary mapping an employee's ID (string) to a list of their direct reports/connections (strings).
- `root`: The starting CEO ID (string).

**Output:**

- Return a list of employee IDs in the exact order they are visited according to the BFS algorithm.

### Example

```python
graph = {
    '1': ['2', '3', '4'],
    '2': ['1', '5', '6'],
    '3': ['1', '7', '8'],
    '4': ['1', '9', '10'],
    '5': ['2'],
    '6': ['2', '11'],
    '7': ['3'],
    '8': ['3'],
    '9': ['4'],
    '10': ['4'],
    '11': ['6']
}

print(Solution().bfs(graph, '1'))
# Output: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
```
