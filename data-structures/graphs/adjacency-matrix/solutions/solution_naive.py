from typing import List, Tuple


class AdjacencyMatrixFriendRecommendation:
    """
    Finds friend recommendations by maintaining an adjacency matrix.
    Uses list comprehensions for concise syntax.
    """

    def __init__(self, users: int, edges: List[Tuple[int, int]]):
        self.users = users
        self.edges = edges
        self.matrix = self._build_matrix()

    def _build_matrix(self) -> List[List[int]]:
        matrix = [[0] * self.users for _ in range(self.users)]
        for u, v in self.edges:
            matrix[u][v] = matrix[v][u] = 1
        return matrix

    def find_recommendations(self) -> List[Tuple[int, int]]:
        recommendations = []
        for i in range(self.users):
            for j in range(i + 1, self.users):
                if self.matrix[i][j] == 0 and any(
                    (self.matrix[i][k] == 1 and self.matrix[k][j] == 1)
                    for k in range(self.users)
                ):
                    recommendations.append((i, j))
        return recommendations
