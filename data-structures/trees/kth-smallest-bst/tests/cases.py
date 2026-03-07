from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TestCase:
    id: str
    tree: List[Optional[int]]
    k: int
    expected: int


# --- Problem 2: kthSmallest Test Cases ---
TEST_CASES = [
    TestCase(id="k_1_in_small_tree", tree=[3, 1, 4, None, 2], k=1, expected=1),
    TestCase(
        id="k_3_in_medium_tree", tree=[5, 3, 6, 2, 4, None, None, 1], k=3, expected=3
    ),
    TestCase(
        id="k_1_in_left_linear_tree", tree=[10, 8, None, 6, None, 4], k=1, expected=4
    ),
    TestCase(
        id="k_4_in_right_linear_tree",
        tree=[1, None, 2, None, 3, None, 4],
        k=4,
        expected=4,
    ),
    TestCase(id="k_is_root_element", tree=[5, 2, 8], k=2, expected=5),
    TestCase(
        id="k_is_max_element", tree=[5, 3, 6, 2, 4, None, None, 1], k=6, expected=6
    ),
    TestCase(id="single_element_tree", tree=[1], k=1, expected=1),
    TestCase(
        id="large_balanced_tree_k_middle", tree=[4, 2, 6, 1, 3, 5, 7], k=4, expected=4
    ),
    TestCase(
        id="large_balanced_tree_k_max", tree=[4, 2, 6, 1, 3, 5, 7], k=7, expected=7
    ),
]
