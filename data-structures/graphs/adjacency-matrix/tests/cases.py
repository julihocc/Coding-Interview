from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    users: int
    edges: List[Tuple[int, int]]
    expected: List[Tuple[int, int]]
    name: str = "Test Case"


# Test cases for finding friend recommendations: pairs of users (i, j) with i < j
# who are not friends but share at least one mutual friend.
TEST_CASES = [
    TestCase(
        name="Lesson Example",
        users=4,
        edges=[(0, 1), (1, 2)],  # A-B and B-C
        expected=[(0, 2)],  # A and C have mutual friend B
    ),
    TestCase(
        name="No Recommendations - fully disconnected", users=5, edges=[], expected=[]
    ),
    TestCase(
        name="No Recommendations - fully connected clan",
        users=3,
        edges=[(0, 1), (1, 2), (0, 2)],
        expected=[],  # Everyone already knows everyone
    ),
    TestCase(
        name="Star Graph",
        users=5,
        edges=[(0, 1), (0, 2), (0, 3), (0, 4)],  # 0 is the center
        expected=[
            (1, 2),
            (1, 3),
            (1, 4),
            (2, 3),
            (2, 4),
            (3, 4),
        ],  # All outer nodes share center
    ),
    TestCase(
        name="Linear Chain",
        users=5,
        edges=[(0, 1), (1, 2), (2, 3), (3, 4)],
        expected=[(0, 2), (1, 3), (2, 4)],  # i and i+2 share i+1
    ),
    TestCase(
        name="Two disjoint components",
        users=6,
        edges=[(0, 1), (1, 2), (3, 4), (4, 5)],  # 0-1-2 and 3-4-5
        expected=[(0, 2), (3, 5)],
    ),
]
