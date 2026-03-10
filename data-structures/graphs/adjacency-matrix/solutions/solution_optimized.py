from typing import List, Tuple


class AdjacencyMatrixFriendRecommendation:
    """
    Finds friend recommendations by checking mutual connections in an adjacency matrix.
    """

    def __init__(self, users: int, edges: List[Tuple[int, int]]):
        self.users = users
        self.edges = edges
        self.matrix = self._build_matrix()

    def _build_matrix(self) -> List[List[int]]:
        # Initialize an empty matrix
        matrix = [[0] * self.users for _ in range(self.users)]

        # Populate friendships (undirected graph)
        for u, v in self.edges:
            matrix[u][v] = 1
            matrix[v][u] = 1

        return matrix

    def find_recommendations(self) -> List[Tuple[int, int]]:
        recommendations = []

        # Check all possible pairs (i, j) where i < j ensures we don't duplicate pairs
        for i in range(self.users):
            for j in range(i + 1, self.users):
                # We only recommend if they are not currently friends
                if self.matrix[i][j] == 0:
                    # Check if there is a mutual friend k
                    for k in range(self.users):
                        if self.matrix[i][k] == 1 and self.matrix[k][j] == 1:
                            recommendations.append((i, j))
                            break  # Move to next pair once one mutual friend is found

        return recommendations
