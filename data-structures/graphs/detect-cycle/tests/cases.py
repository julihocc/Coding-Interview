from dataclasses import dataclass
from typing import Dict, List

@dataclass
class TestCase:
    id: str
    graph: Dict[str, List[str]]
    expected: bool

# --- Problem: detect-cycle Test Cases ---
TEST_CASES = [
    TestCase(
        id="example_1_with_cycle_disconnected",
        graph={
            'A': ['B', 'C'],
            'B': ['A'],
            'C': ['A', 'D'],
            'D': ['C'],
            'E': ['G', 'K'],
            'K': ['G', 'E'],
            'G': ['K', 'E']
        },
        expected=True,
    ),
    TestCase(
        id="example_2_no_cycle",
        graph={
            'A': ['B'],
            'B': ['A', 'C'],
            'C': ['B']
        },
        expected=False,
    ),
    TestCase(
        id="graph_single_cycle",
        graph={
            '1': ['2', '3'],
            '2': ['1', '3'],
            '3': ['1', '2']
        },
        expected=True,
    ),
    TestCase(
        id="graph_empty",
        graph={},
        expected=False,
    ),
    TestCase(
        id="graph_single_node",
        graph={'A': []},
        expected=False,
    ),
    TestCase(
        id="graph_two_components_no_cycle",
        graph={
            'A': ['B'],
            'B': ['A'],
            'C': ['D'],
            'D': ['C']
        },
        expected=False,
    ),
    TestCase(
        id="graph_two_components_one_cycle",
        graph={
            'A': ['B'],
            'B': ['A'],
            'C': ['D', 'E'],
            'D': ['C', 'E'],
            'E': ['C', 'D']
        },
        expected=True,
    ),
]
