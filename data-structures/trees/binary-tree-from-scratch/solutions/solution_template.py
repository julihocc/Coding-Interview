"""TEMPLATE: Binary Tree From Scratch — Build and In-Order Traverse

This is a synthesis exercise. You must complete all four TODOs:

  1. Define your Node class.
  2. Construct the binary tree shown in README.md using your Node class.
  3. Implement in-order traversal (left → root → right).
  4. Return (don't print) the node values as a list[int].

Reference: See ../README.md for the target tree structure and expected output.
"""


class Solution:
    def build_and_traverse(self) -> list[int]:
        """Build a binary tree and return its in-order traversal.

        Target tree:
                4
               / \\
              2   6
             / \\ / \\
            1  3 5  7

        Expected in-order output: [1, 2, 3, 4, 5, 6, 7]
        """

        # TODO 1: Define your Node class
        # class Node:
        #     def __init__(self, value):
        #         ...

        # TODO 2: Build the binary tree
        # root = Node(4)
        # root.left = ...

        # TODO 3: Implement in-order traversal
        # def in_order(node, result):
        #     ...

        # TODO 4: Collect and return the traversal result
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
