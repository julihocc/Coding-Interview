from typing import List, Tuple


class AdjacencyMatrixFriendRecommendation:
    """
    Template for finding friend recommendations using an adjacency matrix.
    """

    def __init__(self, users: int, edges: List[Tuple[int, int]]):
        """
        Initializes the state.

        Args:
            users (int): The total number of users, from 0 to users - 1.
            edges (List[Tuple[int, int]]): The friendship connections.
        """
        self.users = users
        self.edges = edges
        self.matrix = self._build_matrix()

    def _build_matrix(self) -> List[List[int]]:
        """
        Builds the N x N adjacency matrix where 1 means users i and j are friends.

        Returns:
            List[List[int]]: The square adjacency matrix.
        """
        pass

    def find_recommendations(self) -> List[Tuple[int, int]]:
        """
        Finds all (i, j) where i < j, i and j are not friends,
        but they share at least one mutual friend.

        Returns:
            List[Tuple[int, int]]: A sorted list of (i, j) representing friend recommendations.
        """
        pass
