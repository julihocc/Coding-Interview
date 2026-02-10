from dataclasses import dataclass
from typing import List, Optional, Tuple

@dataclass
class TestCase:
    id: str
    operations: List[str]
    values: List[Optional[int]]
    expected: List[Optional[int]]

TEST_CASES = [
    TestCase(
        id="Example",
        operations=["push", "push", "push", "get_min", "pop", "top", "get_min"],
        values=[5, 2, 4, None, None, None, None],
        expected=[None, None, None, 2, None, 2, 2]
    ),
    TestCase(
        id="Single element",
        operations=["push", "get_min", "top", "pop"],
        values=[1, None, None, None],
        expected=[None, 1, 1, None]
    ),
    TestCase(
        id="Descending values",
        operations=["push", "get_min", "push", "get_min", "push", "get_min"],
        values=[3, None, 2, None, 1, None],
        expected=[None, 3, None, 2, None, 1]
    ),
    TestCase(
        id="Ascending values",
        operations=["push", "push", "push", "get_min", "pop", "get_min", "pop", "get_min"],
        values=[1, 2, 3, None, None, None, None, None],
        expected=[None, None, None, 1, None, 1, None, 1]
    ),
    TestCase(
        id="Duplicate minimums",
        operations=["push", "push", "push", "get_min", "pop", "get_min"],
        values=[2, 2, 2, None, None, None],
        expected=[None, None, None, 2, None, 2]
    ),
    TestCase(
        id="Complex operations",
        operations=["push", "push", "get_min", "push", "get_min", "pop", "get_min", "pop"],
        values=[5, 2, None, -1, None, None, None, None],
        expected=[None, None, 2, None, -1, None, 2, None]
    ),
    TestCase(
        id="Negative values",
        operations=["push", "push", "push", "get_min", "pop", "get_min"],
        values=[-5, -10, -3, None, None, None],
        expected=[None, None, None, -10, None, -10]
    ),
    TestCase(
        id="Stock prices scenario",
        operations=["push", "get_min", "push", "get_min", "push", "get_min", "pop", "get_min"],
        values=[100, None, 80, None, 60, None, None, None],
        expected=[None, 100, None, 80, None, 60, None, 80]
    ),
    TestCase(
        id="Empty stack operations",
        operations=["push", "pop", "top", "get_min"],
        values=[1, None, None, None],
        expected=[None, None, None, None]
    ),
]
