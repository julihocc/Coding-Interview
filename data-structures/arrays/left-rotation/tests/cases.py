from dataclasses import dataclass
from typing import List

@dataclass
class TestCase:
    id: str
    n: int
    d: int
    a: List[int]
    expected: List[int]

# Sample cases from problem description + edge cases
TEST_CASES = [
    TestCase(
        id="Sample",
        n=5, 
        d=4,
        a=[1, 2, 3, 4, 5],
        expected=[5, 1, 2, 3, 4]
    ),
    TestCase(
        id="Small Rotation",
        n=5,
        d=2,
        a=[1, 2, 3, 4, 5],
        expected=[3, 4, 5, 1, 2]
    ),
    TestCase(
        id="Full Rotation",
        n=3,
        d=3,
        a=[1, 2, 3],
        expected=[1, 2, 3]
    ),
    TestCase(
        id="Zero Rotation",
        n=3,
        d=0,
        a=[1, 2, 3],
        expected=[1, 2, 3]
    ),
    TestCase(
        id="Large D",
        n=3,
        d=10, # 10 % 3 = 1
        a=[1, 2, 3],
        expected=[2, 3, 1]
    )
]
