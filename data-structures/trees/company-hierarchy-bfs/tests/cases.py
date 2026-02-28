"""
Test cases for Company Hierarchy BFS.
"""

from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class TestCase:
    name: str
    input: Tuple[Dict[str, List[str]], str]
    expected: List[str]


TEST_CASES = [
    TestCase(
        name="Company hierarchy starting from CEO",
        input=(
            {
                "1": ["2", "3", "4"],
                "2": ["1", "5", "6"],
                "3": ["1", "7", "8"],
                "4": ["1", "9", "10"],
                "5": ["2"],
                "6": ["2", "11"],
                "7": ["3"],
                "8": ["3"],
                "9": ["4"],
                "10": ["4"],
                "11": ["6"],
            },
            "1",
        ),
        expected=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"],
    ),
    TestCase(
        name="Small startup hierarchy",
        input=(
            {
                "CEO": ["CTO", "CMO"],
                "CTO": ["CEO", "Dev"],
                "CMO": ["CEO"],
                "Dev": ["CTO"],
            },
            "CEO",
        ),
        expected=["CEO", "CTO", "CMO", "Dev"],
    ),
]
