from dataclasses import dataclass
from typing import List

@dataclass
class TestCase:
    id: str
    nums: List[int]
    expected: List[int]

TEST_CASES = [
    TestCase(
        id="Already sorted",
        nums=[1, 2, 3, 4, 5],
        expected=[1, 2, 3, 4, 5],
    ),
    TestCase(
        id="Reverse order",
        nums=[5, 4, 3, 2, 1],
        expected=[1, 2, 3, 4, 5],
    ),
    TestCase(
        id="Random order",
        nums=[3, 1, 4, 1, 5, 9, 2, 6],
        expected=[1, 1, 2, 3, 4, 5, 6, 9],
    ),
    TestCase(
        id="Duplicates",
        nums=[4, 1, 3, 4, 2, 1],
        expected=[1, 1, 2, 3, 4, 4],
    ),
    TestCase(
        id="Negatives and positives",
        nums=[-3, 0, 2, -1, 5, -10],
        expected=[-10, -3, -1, 0, 2, 5],
    ),
    TestCase(
        id="All equal",
        nums=[7, 7, 7, 7],
        expected=[7, 7, 7, 7],
    ),
    TestCase(
        id="Two elements ascending",
        nums=[1, 2],
        expected=[1, 2],
    ),
    TestCase(
        id="Two elements descending",
        nums=[2, 1],
        expected=[1, 2],
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
    TestCase(
        id="Large array",
        nums=[64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 23, 36, 18, 77],
        expected=[11, 12, 18, 22, 23, 25, 34, 36, 45, 50, 64, 77, 88, 90],
    ),
]
