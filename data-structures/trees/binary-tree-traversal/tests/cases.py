from dataclasses import dataclass
from typing import Optional


class Node:
    """A node in a binary tree."""
    def __init__(self, value: int):
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


def _build_lesson_tree() -> Node:
    """Build the 3-level binary tree from the lesson material.

    Structure:
            1
           / \\
          2   3
         / \\   \\
        4   5   6

    In-order: [4, 2, 5, 1, 3, 6]
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    return root


def _build_left_chain() -> Node:
    """3 -> 2 -> 1 (all left children).  In-order: [1, 2, 3]"""
    root = Node(3)
    root.left = Node(2)
    root.left.left = Node(1)
    return root


def _build_right_chain() -> Node:
    """1 -> 2 -> 3 (all right children).  In-order: [1, 2, 3]"""
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    return root


def _build_two_left() -> Node:
    """Root(5) with left child Node(3).  In-order: [3, 5]"""
    root = Node(5)
    root.left = Node(3)
    return root


def _build_two_right() -> Node:
    """Root(5) with right child Node(8).  In-order: [5, 8]"""
    root = Node(5)
    root.right = Node(8)
    return root


@dataclass
class TestCase:
    id: str
    root: Optional[Node]
    expected: list


TEST_CASES = [
    TestCase(
        id="lesson_example_three_levels",
        root=_build_lesson_tree(),
        expected=[4, 2, 5, 1, 3, 6],
    ),
    TestCase(
        id="empty_tree",
        root=None,
        expected=[],
    ),
    TestCase(
        id="single_node",
        root=Node(7),
        expected=[7],
    ),
    TestCase(
        id="left_only_chain",
        root=_build_left_chain(),
        expected=[1, 2, 3],
    ),
    TestCase(
        id="right_only_chain",
        root=_build_right_chain(),
        expected=[1, 2, 3],
    ),
    TestCase(
        id="two_nodes_left_child",
        root=_build_two_left(),
        expected=[3, 5],
    ),
    TestCase(
        id="two_nodes_right_child",
        root=_build_two_right(),
        expected=[5, 8],
    ),
]
