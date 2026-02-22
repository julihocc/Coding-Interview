from dataclasses import dataclass
from typing import Optional


class Node:
    """A node in a non-binary (multi-way) tree."""
    def __init__(self, value: int):
        self.value = value
        self.children: list["Node"] = []


def _build_lesson_tree() -> Node:
    """Build the 3-level non-binary tree from the lesson material.

    Structure:
             1
           / | \\
          2  3  4
         / \\    |
        5   6   7

    Level-order: [1, 2, 3, 4, 5, 6, 7]
    """
    root = Node(1)
    root.children = [Node(2), Node(3), Node(4)]
    root.children[0].children = [Node(5), Node(6)]
    root.children[2].children = [Node(7)]
    return root


def _build_single_child() -> Node:
    """Root(10) with one child Node(20).  Level-order: [10, 20]"""
    root = Node(10)
    root.children.append(Node(20))
    return root


def _build_wide_tree() -> Node:
    """Root(1) with four children, no grandchildren.  Level-order: [1,2,3,4,5]"""
    root = Node(1)
    root.children = [Node(2), Node(3), Node(4), Node(5)]
    return root


def _build_chain() -> Node:
    """Chain: 1 -> 2 -> 3 (each has one child).  Level-order: [1, 2, 3]"""
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.children.append(b)
    b.children.append(c)
    return a


@dataclass
class TestCase:
    id: str
    root: Optional[Node]
    expected: list


TEST_CASES = [
    TestCase(
        id="lesson_example",
        root=_build_lesson_tree(),
        expected=[1, 2, 3, 4, 5, 6, 7],
    ),
    TestCase(
        id="empty_tree",
        root=None,
        expected=[],
    ),
    TestCase(
        id="single_node",
        root=Node(42),
        expected=[42],
    ),
    TestCase(
        id="root_with_one_child",
        root=_build_single_child(),
        expected=[10, 20],
    ),
    TestCase(
        id="root_with_four_children_no_grandchildren",
        root=_build_wide_tree(),
        expected=[1, 2, 3, 4, 5],
    ),
    TestCase(
        id="chain_single_child_each",
        root=_build_chain(),
        expected=[1, 2, 3],
    ),
]
