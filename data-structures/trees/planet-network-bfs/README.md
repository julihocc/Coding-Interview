# Planetary Network Breadth-First Search (BFS)

Great job, Space Voyager! You've just seen how the Breadth-First Search algorithm operates on a graph representing a network of planets.

Now, let's suppose that the starting point for our BFS traversal isn't Mars but rather Saturn. A mischievous cosmic wind at play, perhaps? Could you modify the code for us so that we can correct our flight path and kickstart the BFS traversal from Saturn instead?

Buckle up! Let's embark on this galactic journey together.

## Problem Statement

Given an adjacency list representing an interconnected network of planets, implement the Breadth-First Search (BFS) algorithm to plan your route starting from a specific planet.

**Input:**

- `graph`: A dictionary mapping planet names (strings) to a list of neighboring planet names.
- `root`: The starting planet name (string). For this mission, your root will be `'Saturn'`.

**Output:**

- Return a list of planet names in the exact order they are visited according to the BFS algorithm.

### Example

```python
graph = {
  'Mars' : ['Jupiter', 'Saturn'],
  'Jupiter' : ['Mars', 'Neptune', 'Uranus'],
  'Saturn' : ['Mars', 'Venus', 'Mercury'],
  'Neptune' : ['Jupiter'],
  'Uranus' : ['Jupiter', 'Earth'],
  'Venus' : ['Saturn'],
  'Mercury' : ['Saturn'],
  'Earth' : ['Uranus']
}

print("Order of visited planets: ", Solution().bfs(graph, 'Saturn'))
# Output: ['Saturn', 'Mars', 'Venus', 'Mercury', 'Jupiter', 'Neptune', 'Uranus', 'Earth']
```
