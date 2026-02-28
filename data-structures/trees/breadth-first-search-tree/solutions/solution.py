from collections import deque
from typing import Dict, List


class Solution:
    def bfs(self, tree: Dict[str, List[str]], root: str) -> List[str]:
        visited = set()  # Set to keep track of visited nodes
        visit_order = []  # List to keep visited nodes in order they are visited
        queue = deque()  # A queue to add nodes for visiting

        queue.append(root)  # We'll start at the root

        while queue:  # While there are nodes to visit.
            node = queue.popleft()  # Visit the first node in the queue

            # Since the tree might have back-edges like 'B' : ['A', 'E'],
            # we should avoid processing already visited nodes
            if node not in visited:
                visit_order.append(node)  # Add it to the list of visited nodes
                visited.add(node)  # And mark the node as visited

                # Now add all unvisited children to the queue
                for child in tree.get(node, []):
                    if child not in visited:
                        queue.append(child)

        return visit_order  # Return the order of visited nodes
