"""TEMPLATE: Binary Tree From Scratch — Build and In-Order Traverse

This is a synthesis exercise. You must complete all four TODOs:

  1. Define your Node class.
  2. Construct the binary tree shown in README.md using your Node class.
  3. Implement in-order traversal (left → root → right).
  4. Return (don't print) the node values as a list[int].

Reference: See ../README.md for the target tree structure and expected output.
"""


class Solution:
    def build_and_inorder(self) -> list[int]:
        """Build the BST and return its IN-ORDER traversal (Left → Root → Right).

        Steps:
          1. Define a Node class with value, left, right.
          2. Build the tree from README.md.
          3. Implement in-order traversal → returns [1, 2, 3, 4, 5, 6, 7].
        """
        # TODO: Implement your solution here
        raise NotImplementedError("Solution not implemented yet")

    def build_and_preorder(self) -> list[int]:
        """Build the BST and return its PRE-ORDER traversal (Root → Left → Right).

        Expected output: [4, 2, 1, 3, 6, 5, 7]
        """
        # TODO: Implement your solution here
        raise NotImplementedError("Solution not implemented yet")

    def build_and_postorder(self) -> list[int]:
        """Build the BST and return its POST-ORDER traversal (Left → Right → Root).

        Expected output: [1, 3, 2, 5, 7, 6, 4]
        """
        # TODO: Implement your solution here
        raise NotImplementedError("Solution not implemented yet")

    # Alias kept for convenience
    def build_and_traverse(self) -> list[int]:
        return self.build_and_inorder()


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
