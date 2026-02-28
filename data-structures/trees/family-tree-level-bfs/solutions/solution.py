from collections import deque
from typing import Dict, List


class Solution:
    def bfs_level(self, graph: Dict[str, List[str]], root: str = "1") -> Dict[str, int]:
        visited = []
        queue = deque()
        queue.append(root)

        level = {root: 0}  # initialize levels dictionary

        while queue:
            vertex = queue.popleft()
            visited.append(vertex)

            level_of_vertex = level[vertex]  # set the current level of vertex

            for child in graph.get(vertex, []):
                if child not in visited and child not in queue:
                    queue.append(child)
                    level[child] = level_of_vertex + 1  # set the level of the child

        # print("\nTraversing completed!")
        return level
