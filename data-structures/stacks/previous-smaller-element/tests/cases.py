from dataclasses import dataclass
from typing import List

@dataclass
class TestCase:
    id: str
    numbers: List[int]
    expected: List[int]

TEST_CASES = [
    TestCase(
        id="Example",
        numbers=[4, 5, 2, 10, 8],
        expected=[-1, 4, -1, 2, 2]
    ),
    TestCase(
        id="Empty array",
        numbers=[],
        expected=[]
    ),
    TestCase(
        id="Single element",
        numbers=[5],
        expected=[-1]
    ),
    TestCase(
        id="Ascending order",
        numbers=[1, 2, 3, 4, 5],
        expected=[-1, 1, 2, 3, 4]
    ),
    TestCase(
        id="Descending order",
        numbers=[5, 4, 3, 2, 1],
        expected=[-1, -1, -1, -1, -1]
    ),
    TestCase(
        id="All equal",
        numbers=[3, 3, 3, 3],
        expected=[-1, -1, -1, -1]
    ),
    TestCase(
        id="Duplicates with smaller",
        numbers=[4, 5, 5, 2, 2, 10],
        expected=[-1, 4, 4, -1, -1, 2]
    ),
    TestCase(
        id="Mixed positive negative",
        numbers=[3, -1, 5, -2, 7],
        expected=[-1, -1, -1, -1, -2]
    ),
    TestCase(
        id="Stock prices example",
        numbers=[100, 80, 60, 70, 60, 75, 85],
        expected=[-1, -1, -1, 60, -1, 60, 75]
    ),
]
