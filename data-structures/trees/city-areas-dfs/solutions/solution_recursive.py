"""Complete solution for City Areas DFS — Build and Traverse from Scratch.

Implements:
  - CityNode.add_area(): creates and appends a child CityNode
  - CityNode.dfs(): recursive pre-order DFS with visited set
  - Solution.build_and_traverse(): constructs the city hierarchy and runs DFS
"""

from tests.cases import CityNode


class Solution:
    def build_and_traverse(self) -> list[str]:
        """Build the city hierarchy and return DFS traversal order.

        Time Complexity:  O(n) — every area node visited exactly once.
        Space Complexity: O(n) — visited set + result list + O(h) call stack.

        City hierarchy:
            City Center
            ├── North District → Elm Suburb, Oak Suburb
            ├── East District  → Pine Suburb, Maple Suburb
            └── South District → Cedar Suburb
        """
        # Build the tree
        city = CityNode("City Center")
        city.add_area("North District")
        city.add_area("East District")
        city.add_area("South District")

        north = city.areas[0]
        north.add_area("Elm Suburb")
        north.add_area("Oak Suburb")

        east = city.areas[1]
        east.add_area("Pine Suburb")
        east.add_area("Maple Suburb")

        south = city.areas[2]
        south.add_area("Cedar Suburb")

        # Traverse and return
        return city.dfs()
