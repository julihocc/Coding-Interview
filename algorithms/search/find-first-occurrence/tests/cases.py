from dataclasses import dataclass
from typing import List

@dataclass
class TestCase:
    id: str
    target: int
    nums: List[int]
    expected: int

TEST_CASES = [
    TestCase(
        id="Example",
        target=3,
        nums=[1, 2, 3, 4, 5],
        expected=2
    ),
    TestCase(
        id="Sample 1",
        target=3,
        nums=[3],
        expected=0
    ),
    TestCase(
        id="Sample 0",
        target=5,
        nums=[],
        expected=-1
    ),
    TestCase(
        id="Duplicates",
        target=2,
        nums=[1, 2, 2, 2, 3],
        expected=1
    ),
    TestCase(
        id="First Element",
        target=1,
        nums=[1, 2, 3],
        expected=0
    ),
    TestCase(
        id="Not Found",
        target=10,
        nums=[1, 2, 3],
        expected=-1
    ),
    TestCase(
        id="All Equal",
        target=5,
        nums=[5, 5, 5, 5],
        expected=0
    )
]
