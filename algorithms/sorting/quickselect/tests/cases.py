from dataclasses import dataclass
from typing import List

@dataclass
class TestCase:
    id: str
    nums: List[int]
    k: int
    expected: int

TEST_CASES = [
    TestCase(
        id="Smallest element",
        nums=[7, 2, 1, 8, 6, 3, 5, 4],
        k=0,
        expected=1,
    ),
    TestCase(
        id="Middle element",
        nums=[7, 2, 1, 8, 6, 3, 5, 4],
        k=4,
        expected=5,
    ),
    TestCase(
        id="With duplicates",
        nums=[3, 1, 2, 2, 4],
        k=2,
        expected=2,
    ),
    TestCase(
        id="Negatives and positives",
        nums=[-5, -10, 0, 5, 2],
        k=1,
        expected=-5,
    ),
    TestCase(
        id="Single element",
        nums=[42],
        k=0,
        expected=42,
    ),
    TestCase(
        id="Largest element",
        nums=[9, 8, 7, 6, 5],
        k=4,
        expected=9,
    ),
]
