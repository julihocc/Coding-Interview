from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TestCase:
    id: str
    tree: List[Optional[int]]
    k: int
    expected: int


# --- Problem: kth-largest-bst Test Cases ---
TEST_CASES = [
    TestCase(
        id="example_1",
        tree=[50, 20, 60, 10, 30, 55, 70, None, None, 25, 35, None, None, 65, 80],
        k=1,
        expected=80,
    ),
    TestCase(
        id="example_k5",
        tree=[50, 20, 60, 10, 30, 55, 70, None, None, 25, 35, None, None, 65, 80],
        k=5,
        expected=55,
    ),
    # Let's verify the full sorted descending array of the example tree:
    # 80, 70, 65, 60, 55, 50, 35, 30, 25, 20, 10.
    TestCase(
        id="example_k10",
        tree=[50, 20, 60, 10, 30, 55, 70, None, None, 25, 35, None, None, 65, 80],
        k=10,
        expected=20,
    ),
    TestCase(
        id="example_k3",
        tree=[50, 20, 60, 10, 30, 55, 70, None, None, 25, 35, None, None, 65, 80],
        k=3,
        expected=65,
    ),
    TestCase(
        id="example_k7",
        tree=[50, 20, 60, 10, 30, 55, 70, None, None, 25, 35, None, None, 65, 80],
        k=7,
        expected=35,
    ),
    TestCase(id="single_node_k1", tree=[5], k=1, expected=5),
    TestCase(
        id="skewed_left_k2", tree=[10, 8, None, 6, None, 4, None, 2], k=2, expected=8
    ),
    TestCase(
        id="skewed_right_k3",
        tree=[1, None, 2, None, 3, None, 4, None, 5],
        k=3,
        expected=3,
    ),
]
