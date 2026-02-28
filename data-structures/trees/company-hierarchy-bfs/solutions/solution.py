from collections import deque
from typing import Dict, List


class Solution:
    def bfs(self, graph: Dict[str, List[str]], root: str = "1") -> List[str]:
        visited = []  # List to keep track of visited nodes
        queue = deque()
        queue.append(root)  # Start with the root node

        while queue:
            vertex = queue.popleft()

            # Bug Fix: Ensure we don't process already visited vertices
            # Also, properly append the popped vertex to visited
            if vertex not in visited:
                visited.append(vertex)

                # Add all unvisited children to the queue
                for child in graph.get(vertex, []):
                    # Bug Fix: Prevent adding to queue if it's already there or visited
                    if child not in visited and child not in queue:
                        queue.append(child)

        return visited
