"""
Test cases for Network Concept BFS.
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
        name="Standard computer network",
        input=(
            {
                "computer": ["printer", "router"],
                "printer": ["paper", "computer"],
                "router": ["internet", "computer"],
                "internet": ["data", "router"],
                "paper": ["printer"],
                "data": ["internet"],
            },
            "computer",
        ),
        expected=["computer", "printer", "router", "paper", "internet", "data"],
    ),
    TestCase(
        name="Network starting from router",
        input=(
            {
                "computer": ["printer", "router"],
                "printer": ["paper", "computer"],
                "router": ["internet", "computer"],
                "internet": ["data", "router"],
                "paper": ["printer"],
                "data": ["internet"],
            },
            "router",
        ),
        expected=["router", "internet", "computer", "data", "printer", "paper"],
    ),
    TestCase(name="Single node", input=({"server": []}, "server"), expected=["server"]),
]
