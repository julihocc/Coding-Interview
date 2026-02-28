"""
Test cases for Planetary Network BFS.
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
        name="BFS starting from Saturn",
        input=(
            {
                "Mars": ["Jupiter", "Saturn"],
                "Jupiter": ["Mars", "Neptune", "Uranus"],
                "Saturn": ["Mars", "Venus", "Mercury"],
                "Neptune": ["Jupiter"],
                "Uranus": ["Jupiter", "Earth"],
                "Venus": ["Saturn"],
                "Mercury": ["Saturn"],
                "Earth": ["Uranus"],
            },
            "Saturn",
        ),
        expected=[
            "Saturn",
            "Mars",
            "Venus",
            "Mercury",
            "Jupiter",
            "Neptune",
            "Uranus",
            "Earth",
        ],
    ),
    TestCase(
        name="BFS starting from Mars",
        input=(
            {
                "Mars": ["Jupiter", "Saturn"],
                "Jupiter": ["Mars", "Neptune", "Uranus"],
                "Saturn": ["Mars", "Venus", "Mercury"],
                "Neptune": ["Jupiter"],
                "Uranus": ["Jupiter", "Earth"],
                "Venus": ["Saturn"],
                "Mercury": ["Saturn"],
                "Earth": ["Uranus"],
            },
            "Mars",
        ),
        expected=[
            "Mars",
            "Jupiter",
            "Saturn",
            "Neptune",
            "Uranus",
            "Venus",
            "Mercury",
            "Earth",
        ],
    ),
    TestCase(
        name="Single planet network", input=({"Pluto": []}, "Pluto"), expected=["Pluto"]
    ),
]
