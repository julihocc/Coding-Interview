from collections import deque
from typing import Dict, List


class Solution:
    def bfs(self, tree: Dict[str, List[str]], root: str) -> List[str]:
        # Implement BFS for the given tree, starting at node `root`
        visited = []
        queue = deque()
        queue.append(root)

        while queue:
            vertex = queue.popleft()

            # Record visitation and enqueue neighbors
            if vertex not in visited:
                visited.append(vertex)

                for child in tree.get(vertex, []):
                    if child not in visited and child not in queue:
                        queue.append(child)

        # Return the list of tree nodes in the order they were visited
        return visited
