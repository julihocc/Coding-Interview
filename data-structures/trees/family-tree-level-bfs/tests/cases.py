"""
Test cases for Family Tree Level BFS.
"""

from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class TestCase:
    name: str
    input: Tuple[Dict[str, List[str]], str]
    expected: Dict[str, int]


TEST_CASES = [
    TestCase(
        name="Royal family tree",
        input=(
            {
                "1": ["2", "3", "4"],
                "2": ["5", "6"],
                "3": ["7"],
                "4": ["8", "9"],
                "5": [],
                "6": ["10"],
                "7": ["11", "12"],
                "8": [],
                "9": [],
                "10": [],
                "11": [],
                "12": [],
            },
            "1",
        ),
        expected={
            "1": 0,
            "2": 1,
            "3": 1,
            "4": 1,
            "5": 2,
            "6": 2,
            "7": 2,
            "8": 2,
            "9": 2,
            "10": 3,
            "11": 3,
            "12": 3,
        },
    ),
    TestCase(
        name="Linear dynasty",
        input=({"A": ["B"], "B": ["C"], "C": ["D"], "D": []}, "A"),
        expected={"A": 0, "B": 1, "C": 2, "D": 3},
    ),
    TestCase(name="Single monarch", input=({"King": []}, "King"), expected={"King": 0}),
]
