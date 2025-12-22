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
        id="Sample 1",
        target=3,
        nums=[1, 2, 3, 4, 5],
        expected=2
    ),
    TestCase(
        id="Sample 2",
        target=16,
        nums=[2, 4, 6, 8, 10, 12, 14, 16],
        expected=7
    ),
    TestCase(
        id="Not Found",
        target=100,
        nums=[1, 2, 3],
        expected=-1
    ),
    TestCase(
        id="Empty",
        target=1,
        nums=[],
        expected=-1
    ),
    TestCase(
        id="Start",
        target=10,
        nums=[10, 20, 30],
        expected=0
    ),
    TestCase(
        id="End",
        target=30,
        nums=[10, 20, 30],
        expected=2
    )
]
