"""
Test cases for Breadth-first Search on Trees.
"""

from dataclasses import dataclass
from typing import Dict, List, Any, Tuple


@dataclass
class TestCase:
    name: str
    input: Tuple[Dict[str, List[str]], str]
    expected: List[str]


TEST_CASES = [
    TestCase(
        name="Standard complex tree",
        input=(
            {
                "A": ["B", "C", "D"],
                "B": ["A", "E"],
                "C": ["A", "F", "G"],
                "D": ["A", "H"],
                "E": ["B", "I"],
                "F": ["C"],
                "G": ["C", "J"],
                "H": ["D"],
                "I": ["E"],
                "J": ["G"],
            },
            "A",
        ),
        expected=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    ),
    TestCase(
        name="Linear tree (like a linked list)",
        input=({"1": ["2"], "2": ["3"], "3": ["4"], "4": []}, "1"),
        expected=["1", "2", "3", "4"],
    ),
    TestCase(name="Single node tree", input=({"Z": []}, "Z"), expected=["Z"]),
]
