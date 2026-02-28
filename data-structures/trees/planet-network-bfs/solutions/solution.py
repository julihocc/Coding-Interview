from collections import deque
from typing import Dict, List


class Solution:
    def bfs(self, graph: Dict[str, List[str]], root: str = "Saturn") -> List[str]:
        visited = []  # List to keep track of visited nodes
        queue = deque()
        queue.append(root)  # Start with the root node

        while queue:  # While there are nodes to visit.
            vertex = queue.popleft()  # Visit the first node in the queue
            # print(f"{vertex} has been visited")
            visited.append(vertex)  # Add it to the visited nodes list

            for neighbour in graph.get(
                vertex, []
            ):  # Add all unvisited children to the queue
                if neighbour not in visited and neighbour not in queue:
                    queue.append(neighbour)

        return visited
