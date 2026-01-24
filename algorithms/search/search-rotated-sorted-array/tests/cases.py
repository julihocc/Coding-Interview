from dataclasses import dataclass
from typing import List

@dataclass
class TestCase:
    """
    TestCase represents a single test case for the search rotated sorted array
    problem.
    """
    id: str
    nums: List[int]
    target: int
    expected: int


TEST_CASES = [
    TestCase(
        id="example_1",
        nums=[4, 5, 6, 7, 0, 1, 2],
        target=0,
        expected=4
    ),
    TestCase(
        id="example_2",
        nums=[4, 5, 6, 7, 0, 1, 2],
        target=3,
        expected=-1
    ),
    TestCase(
        id="no_rotation",
        nums=[1, 3],
        target=3,
        expected=1
    ),
    TestCase(
        id="single_element_found",
        nums=[1],
        target=1,
        expected=0
    ),
    TestCase(
        id="single_element_not_found",
        nums=[1],
        target=0,
        expected=-1
    ),
    TestCase(
        id="pivot_at_start",
        nums=[1, 2, 3, 4, 5],
        target=2,
        expected=1
    ),
    TestCase(
        id="pivot_at_end",
        nums=[2, 3, 4, 5, 1],
        target=1,
        expected=4
    ),
    TestCase(
        id="target_at_pivot",
        nums=[4, 5, 6, 7, 0, 1, 2],
        target=0,
        expected=4
    ),
    TestCase(
        id="large_rotation",
        nums=[8, 9, 11, 15, 1, 2, 4, 5],
        target=15,
        expected=3
    ),
    TestCase(
        id="large_rotation_not_found",
        nums=[8, 9, 11, 15, 1, 2, 4, 5],
        target=10,
        expected=-1
    ),
    TestCase(
        id="empty_array",
        nums=[],
        target=5,
        expected=-1
    )
]
