from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TestCase:
    id: str
    tree: List[Optional[int]]
    expected: bool


# --- Problem 1: check-bst-balance Test Cases ---
TEST_CASES = [
    TestCase(id="balanced_tree_1", tree=[3, 9, 20, None, None, 15, 7], expected=True),
    TestCase(
        id="unbalanced_tree_1", tree=[1, 2, 2, 3, 3, None, None, 4, 4], expected=False
    ),
    TestCase(id="empty_tree", tree=[], expected=True),
    TestCase(id="single_node", tree=[1], expected=True),
    TestCase(
        id="left_linear_unbalanced", tree=[1, 2, None, 3, None, 4], expected=False
    ),
    TestCase(
        id="right_linear_unbalanced",
        tree=[1, None, 2, None, 3, None, 4],
        expected=False,
    ),
    TestCase(
        id="balanced_large_complete_tree", tree=[1, 2, 3, 4, 5, 6, 7], expected=True
    ),
    TestCase(
        id="unbalanced_leaf_deep",
        tree=[1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None, None, None],
        expected=True,  # Wait, this is unbalanced because left has depth 4 and right depth 3... Actually 4-3 = 1 -> Balanced!
    ),
    TestCase(
        id="unbalanced_deep_difference",
        tree=[
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            None,
            None,
            None,
            None,
            None,
            None,
            10,
            None,
            None,
            None,
        ],
        expected=False,
    ),
]
