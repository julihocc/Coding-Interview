from dataclasses import dataclass
from collections import deque
from typing import List

@dataclass
class TestCase:
    id: str
    q1: List[int]
    q2: List[int]
    expected: List[int]

TEST_CASES = [
    TestCase(
        id="1",
        q1=[1, 2, 3, 4, 5],
        q2=[6, 7, 8, 9, 10],
        expected=[1, 6, 2, 7, 3, 8, 4, 9, 5, 10]
    ),
    TestCase(
        id="2",
        q1=[1],
        q2=[2],
        expected=[1, 2]
    ),
    TestCase(
        id="3",
        q1=[10, 20, 30],
        q2=[40, 50, 60],
        expected=[10, 40, 20, 50, 30, 60]
    ),
    # Large input test case
    TestCase(
        id="4",
        q1=list(range(100)),
        q2=list(range(100, 200)),
        expected=[x for pair in zip(range(100), range(100, 200)) for x in pair]
    ),
]
