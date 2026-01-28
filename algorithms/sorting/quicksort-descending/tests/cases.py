from dataclasses import dataclass
from typing import List

@dataclass
class TestCase:
    id: str
    nums: List[int]
    expected: List[int]

TEST_CASES = [
    TestCase(
        id="Already sorted descending",
        nums=[4, 3, 2, 1],
        expected=[4, 3, 2, 1],
    ),
    TestCase(
        id="Ascending order (reverse)",
        nums=[1, 2, 3, 4, 5],
        expected=[5, 4, 3, 2, 1],
    ),
    TestCase(
        id="Duplicates",
        nums=[4, 1, 3, 4, 2],
        expected=[4, 4, 3, 2, 1],
    ),
    TestCase(
        id="Negatives and positives",
        nums=[-3, 0, 2, -1, 5],
        expected=[5, 2, 0, -1, -3],
    ),
    TestCase(
        id="All equal",
        nums=[7, 7, 7],
        expected=[7, 7, 7],
    ),
    TestCase(
        id="Single element",
        nums=[42],
        expected=[42],
    ),
    TestCase(
        id="Empty",
        nums=[],
        expected=[],
    ),
]
