from dataclasses import dataclass
from typing import List

@dataclass
class TestCase:
    id: str
    arr: List[int]
    expected: int

TEST_CASES = [
    TestCase(
        id="Example",
        arr=[2, 4, 1, 3, 5],
        expected=7
    ),
    TestCase(
        id="Empty array",
        arr=[],
        expected=0
    ),
    TestCase(
        id="Single element",
        arr=[5],
        expected=0
    ),
    TestCase(
        id="Already sorted",
        arr=[1, 2, 3, 4, 5],
        expected=10  # n*(n-1)/2 = 5*4/2 = 10
    ),
    TestCase(
        id="Reverse sorted",
        arr=[5, 4, 3, 2, 1],
        expected=0  # No anti-inversions
    ),
    TestCase(
        id="All equal",
        arr=[3, 3, 3, 3],
        expected=0  # No strict inequalities
    ),
    TestCase(
        id="Duplicates mixed",
        arr=[2, 2, 3, 1, 3],
        expected=5  # (0,2)=2<3, (0,4)=2<3, (1,2)=2<3, (1,4)=2<3, (3,4)=1<3
    ),
    TestCase(
        id="Negative numbers",
        arr=[-3, -1, 0, 2, 5],
        expected=10  # All pairs are anti-inversions
    ),
    TestCase(
        id="Two elements ascending",
        arr=[1, 2],
        expected=1
    ),
    TestCase(
        id="Two elements descending",
        arr=[2, 1],
        expected=0
    ),
    TestCase(
        id="Large range values",
        arr=[-1000000000, 0, 1000000000],
        expected=3  # (0,1), (0,2), (1,2)
    ),
]
