class Solution:
    def has_cycle(self, graph: dict[str, list[str]]) -> bool:
        visited = set()
        for vertex in graph:
            if vertex not in visited:
                if self.dfs(vertex, visited, graph, None):
                    return True
        return False

    def dfs(self, vertex: str, visited: set[str], graph: dict[str, list[str]], parent: str) -> bool:
        visited.add(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                if self.dfs(neighbor, visited, graph, vertex):
                    return True
            elif neighbor != parent:
                return True
                
        return False
