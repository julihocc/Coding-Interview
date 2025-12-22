from dataclasses import dataclass
from typing import List, Union

@dataclass
class TestCase:
    id: str
    x: List[float]
    y: List[float]
    expected: Union[int, List[int]]

TEST_CASES = [
    TestCase(
        id="Sample 1",
        x=[0, 1, 2, 3, 4, 5, 6, 7],
        y=[-2, 0, 4, 5, 6, 7, 8, 9],
        expected=1
    ),
    TestCase(
        id="Sample 2",
        x=[0, 1, 2, 3, 4, 5, 6, 7],
        y=[-2, 0, 4, 4.2, 4.3, 4.5, 8, 9],
        expected=[1, 5] # Logic allows either index where condition holds
    ),
    TestCase(
        id="Sample 3",
        x=[0, 1],
        y=[-10, 10],
        expected=0
    ),
     TestCase(
        id="Sample 4",
        x=[0, 1, 2, 3],
        y=[-10, -9, -8, 5],
        expected=2
    ),
]
