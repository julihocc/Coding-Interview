# Rainforest Breadth-First Search (BFS)

Great job on your space journey thus far, Voyager! You've recently ventured into the exciting realm of the Breadth-First Search (BFS) algorithm, which is applied to non-binary trees. It's now time to apply this knowledge to a real-life scenario.

Suppose you're an explorer charting a course through the world's major rainforests. Starting from the Amazon rainforest, your objective is to explore every neighboring forest. Your task involves using the Breadth-First Search algorithm to plan your route.

## Problem Statement

Given a dictionary representing interconnected forests, implement the Breadth-First Search (BFS) algorithm to plan your route.

**Input:**

- `forest`: A dictionary mapping forest names (strings) to a list of neighboring forest names.
- `root`: The starting forest name (string).

**Output:**

- Return a list of forest names in the exact order they are visited according to the BFS algorithm.

### Example

```python
forest = {
    'Amazon_Rainforest': ['Congo_Basin', 'Southeast_Asian_Rainforests'],
    'Congo_Basin': ['Guinea_Rainforests', 'New_Guinea_Rainforests'],
    'Southeast_Asian_Rainforests': ['Sundaland_Rainforests', 'Wallacea_Rainforests'],
    'Guinea_Rainforests': [],
    'New_Guinea_Rainforests': ['Papua_New_Guinea_Rainforests'],
    'Sundaland_Rainforests': [],
    'Wallacea_Rainforests': ['Celebes_Rainforests'],
    'Papua_New_Guinea_Rainforests': [],
    'Celebes_Rainforests': []
}

print(' -> '.join(Solution().bfs(forest, 'Amazon_Rainforest')))
# Output: Amazon_Rainforest -> Congo_Basin -> Southeast_Asian_Rainforests -> Guinea_Rainforests -> New_Guinea_Rainforests -> Sundaland_Rainforests -> Wallacea_Rainforests -> Papua_New_Guinea_Rainforests -> Celebes_Rainforests
```
