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
        operations=["push", "push", "push", "get_max", "pop", "top", "get_max"],
        values=[1, 5, 3, None, None, None, None],
        expected=[None, None, None, 5, None, 5, 5]
    ),
    TestCase(
        id="Single element",
        operations=["push", "get_max", "top", "pop"],
        values=[1, None, None, None],
        expected=[None, 1, 1, None]
    ),
    TestCase(
        id="Ascending values",
        operations=["push", "get_max", "push", "get_max", "push", "get_max"],
        values=[1, None, 2, None, 3, None],
        expected=[None, 1, None, 2, None, 3]
    ),
    TestCase(
        id="Descending values",
        operations=["push", "push", "push", "get_max", "pop", "get_max", "pop", "get_max"],
        values=[3, 2, 1, None, None, None, None, None],
        expected=[None, None, None, 3, None, 3, None, 3]
    ),
    TestCase(
        id="Duplicate maximums",
        operations=["push", "push", "push", "get_max", "pop", "get_max"],
        values=[5, 5, 5, None, None, None],
        expected=[None, None, None, 5, None, 5]
    ),
    TestCase(
        id="Complex operations",
        operations=["push", "push", "get_max", "push", "get_max", "pop", "get_max", "pop"],
        values=[1, 5, None, -5, None, None, None, None],
        expected=[None, None, 5, None, 5, None, 5, None]
    ),
    TestCase(
        id="Negative values",
        operations=["push", "push", "push", "get_max", "pop", "get_max"],
        values=[-5, -10, -3, None, None, None],
        expected=[None, None, None, -3, None, -5]
    ),
    TestCase(
        id="Empty stack operations",
        operations=["push", "pop", "top", "get_max"],
        values=[1, None, None, None],
        expected=[None, None, None, None]
    ),
]
