"""TEMPLATE: City Areas DFS — Build and Traverse from Scratch

Reference: See ../README.md for full problem description

You need to implement TWO things:
  1. CityNode.add_area()  — create a child node and append to self.areas
  2. CityNode.dfs()       — visit current node, then recurse into each area

Then build the city tree and return the DFS traversal.
"""


class CityNode:
    def __init__(self, name: str):
        self.name = name
        self.areas: list["CityNode"] = []

    def add_area(self, area_name: str) -> None:
        # TODO: Create a new CityNode(area_name) and append to self.areas
        raise NotImplementedError("add_area not implemented yet")

    def dfs(self, visited: set | None = None, result: list | None = None) -> list[str]:
        # TODO: Initialize visited and result if None
        # TODO: Add self.name to visited and result
        # TODO: For each area in self.areas, if not visited, recurse
        raise NotImplementedError("dfs not implemented yet")


class Solution:
    def build_and_traverse(self) -> list[str]:
        """Build the city hierarchy and return DFS traversal order.

        Steps:
          1. Create CityNode('City Center') as root.
          2. Add North District, East District, South District.
          3. Add Elm Suburb, Oak Suburb to North District.
          4. Add Pine Suburb, Maple Suburb to East District.
          5. Add Cedar Suburb to South District.
          6. Call root.dfs() and return the result.
        """
        # TODO: Implement your solution here
        raise NotImplementedError("Solution not implemented yet")


if __name__ == "__main__":
    import sys
    import os

    current_dir = os.path.dirname(os.path.abspath(__file__))
    problem_dir = os.path.dirname(current_dir)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(problem_dir)))

    sys.path.append(project_root)
    sys.path.append(problem_dir)

    from utils.judge_utils import test_solution
    from tests.cases import TEST_CASES

    def run_case_logic(SolutionClass, case):
        instance = SolutionClass()
        result = instance.build_and_traverse()
        return result == case.expected

    test_solution(Solution, TEST_CASES, run_case_logic)
