class Solution:
    def has_cycle(self, graph: dict[str, list[str]]) -> bool:
        visited = set()
        # implement this
        return False

    def dfs(self, vertex: str, visited: set, graph: dict[str, list[str]], parent: str) -> bool:
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited: 
                pass # implement this
                
        return False
