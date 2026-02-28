"""
Test cases for Rainforest BFS.
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
        name="Standard rainforest traversal",
        input=(
            {
                "Amazon_Rainforest": ["Congo_Basin", "Southeast_Asian_Rainforests"],
                "Congo_Basin": ["Guinea_Rainforests", "New_Guinea_Rainforests"],
                "Southeast_Asian_Rainforests": [
                    "Sundaland_Rainforests",
                    "Wallacea_Rainforests",
                ],
                "Guinea_Rainforests": [],
                "New_Guinea_Rainforests": ["Papua_New_Guinea_Rainforests"],
                "Sundaland_Rainforests": [],
                "Wallacea_Rainforests": ["Celebes_Rainforests"],
                "Papua_New_Guinea_Rainforests": [],
                "Celebes_Rainforests": [],
            },
            "Amazon_Rainforest",
        ),
        expected=[
            "Amazon_Rainforest",
            "Congo_Basin",
            "Southeast_Asian_Rainforests",
            "Guinea_Rainforests",
            "New_Guinea_Rainforests",
            "Sundaland_Rainforests",
            "Wallacea_Rainforests",
            "Papua_New_Guinea_Rainforests",
            "Celebes_Rainforests",
        ],
    ),
    TestCase(
        name="Small forest system",
        input=(
            {"Forest_A": ["Forest_B", "Forest_C"], "Forest_B": [], "Forest_C": []},
            "Forest_A",
        ),
        expected=["Forest_A", "Forest_B", "Forest_C"],
    ),
    TestCase(
        name="Single forest",
        input=({"Lonely_Forest": []}, "Lonely_Forest"),
        expected=["Lonely_Forest"],
    ),
]
