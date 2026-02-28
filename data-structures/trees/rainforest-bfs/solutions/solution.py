from collections import deque
from typing import Dict, List


class Solution:
    def bfs(
        self, forest: Dict[str, List[str]], root: str = "Amazon_Rainforest"
    ) -> List[str]:
        """BFS algorithm to visit all forests"""
        queue = deque()  # Queue to hold forest regions
        queue.append(root)  # Starting search from root
        visited = []  # List to hold visited forests

        while queue:
            current_forest = queue.popleft()

            if current_forest not in visited:
                visited.append(current_forest)  # Mark current forest as visited

                # Queuing the forests not yet visited
                if current_forest in forest:
                    for neighbouring_forest in forest[current_forest]:
                        if neighbouring_forest not in visited:
                            queue.append(neighbouring_forest)

        return visited
